from rest_framework import serializers
from friendsapp import models


class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendshipRequest
        fields = ('id', 'from_user', 'to_user',)
        # read_only_fields = ('id', )


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friends
        fields = ('__all__', )
