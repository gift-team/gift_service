from django.contrib.auth.models import Group
from rest_framework import serializers

from authapp.models import GiftUser


class GiftUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GiftUser
        fields = ('id', 'username', 'first_name', 'middle_name', 'last_name', 'address',
                  'email', 'is_superuser' ,'is_staff', 'is_active', 'date_joined', 'age', 'avatar')
        read_only_fields = ('id',)


class GiftGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
