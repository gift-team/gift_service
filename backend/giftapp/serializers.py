from rest_framework import serializers

from giftapp.models import Gift


class GiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gift
        fields = ['id', 'owner', 'name', 'description', 'photo', 'link', 'price', 'collection', ]
        # read_only_fields = ('id', 'owner',)


class CreateGiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ('name', 'description', 'photo', 'link', 'price', 'collection', )

    def create(self, validated_data, request):
        user = request.user
        owner = user.id
        instance = self.Meta.model(owner, **validated_data)
        instance.save()
        return instance
