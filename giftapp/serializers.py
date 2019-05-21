from rest_framework import serializers

from giftapp.models import Products


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'owner', 'name', 'description', 'photo', 'link', 'price', 'collection', ]
        read_only_fields = ('id', 'owner',)
