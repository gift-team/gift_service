from abc import ABC

from rest_framework import serializers
from authapp import models

#! TODO редактирование профиля
#! TODO регистрация пользователя
#! TODO смена пароля


class AddressNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressName
        fields = ('id', 'name')


class AddressCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ('id', 'name')


class AddressRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ('id', 'name')


class AddressCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ('id', 'name')


class AddressStreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Street
        fields = ('id', 'name')


class AddressBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = ('id', 'number', 'structure')


class AddressFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Flat
        fields = ('id', 'number')


class AddressSerializer(serializers.ModelSerializer):
    country = AddressCountrySerializer()
    region = AddressRegionSerializer()
    city = AddressCitySerializer()
    street = AddressStreetSerializer()
    building = AddressBuildingSerializer()
    flat = AddressFlatSerializer()

    class Meta:
        model = models.Address
        # fields = ('country', 'region', 'city', 'street', 'building', 'flat')
        fields = ('id', 'country', 'region', 'city', 'street', 'building', 'flat')


class AddressListSerializer(serializers.ModelSerializer):
    name = AddressNameSerializer()
    address = AddressSerializer()

    class Meta:
        model = models.AddressList
        fields = ('name', 'address')


class ProfileSerializer(serializers.ModelSerializer):
    address_list = AddressListSerializer(many=True)

    class Meta:
        model = models.GiftUser
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'address_list',
                  'age', 'gender', 'phone', 'avatar', 'login', 'email')


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
