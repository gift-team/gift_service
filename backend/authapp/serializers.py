from rest_framework import serializers
from authapp import models


class AddressListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = models.AddressList
        fields = ('id', 'name', 'country', 'region', 'city', 'street', 'building', 'flat')


class ProfileSerializer(serializers.ModelSerializer):
    address_list = AddressListSerializer(many=True)

    class Meta:
        model = models.GiftUser
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'address_list',
                  'birthdate', 'gender', 'phone', 'avatar', 'login', 'email')
        depth = 1

    def update(self, instance, validated_data):
        address_lst = validated_data.pop('address_list')

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.login = validated_data.get('gender', instance.login)
        instance.save()

        for i in address_lst:
            if 'id' in i:
                address = instance.address_list.get(id=i['id'])
                address.name = i.get('name', address.name)
                address.country = i.get('country', address.country)
                address.region = i.get('region', address.region)
                address.city = i.get('city', address.city)
                address.street = i.get('street', address.street)
                address.building = i.get('building', address.building)
                address.flat = i.get('flat', address.flat)
                address.save()
            else:
                address = instance.address_list.create(
                    name=i['name'],
                    country=i['country'],
                    region = i['region'],
                    city = i['city'],
                    street = i['street'],
                    building = i['building'],
                    flat = i['flat']
                )
                address.save()

        return instance


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GiftUser
        fields = ('email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
