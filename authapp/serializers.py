from rest_framework import serializers
from authapp.models import GiftUser, AddressList


class AddressListSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    address = serializers.StringRelatedField()

    class Meta:
        model = AddressList
        fields = ('name', 'address')


class GiftUserSerializer(serializers.HyperlinkedModelSerializer):
    address_list = AddressListSerializer(many=True, read_only=True)

    class Meta:
        model = GiftUser
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'address_list',
                  'email', 'password', 'is_superuser', 'is_staff', 'is_active',
                  'date_joined', 'age', 'gender', 'phone', 'avatar')
        read_only_fields = ('id',)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
