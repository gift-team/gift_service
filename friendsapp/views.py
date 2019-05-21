from rest_framework import viewsets, permissions, generics, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from authapp.models import GiftUser
from friendsapp.serializers import FriendsSerializer, FriendshipRequestSerializer
from friendsapp.models import Friends, FriendshipRequest
from gift_service import settings

from django.core import serializers

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class FriendsView(generics.RetrieveAPIView):
    serializer_class = FriendsSerializer

    def get(self, request):
        user = request.user
        friends = Friends.objects.select_related('from_user', 'to_user').filter(to_user=user).all()
        return Response(friends)


class FriendshipRequestView(generics.ListCreateAPIView):
    serializer_class = FriendshipRequestSerializer
    # renderer_classes = (JSONRenderer, )

    def get(self, request):
        user = request.user
        out_requests = FriendshipRequest.objects.filter(from_user=user).all()
        inc_requests = FriendshipRequest.objects.filter(to_user=user).all()
        content = {
            'outgoing_requests': FriendshipRequestSerializer(out_requests, many=True).data,
            'incoming_requests': FriendshipRequestSerializer(inc_requests, many=True).data
        }
        return Response(content)

    def post(self, request):
        from_user = GiftUser.objects.get(pk=request.data['from_user'])
        to_user = GiftUser.objects.get(pk=request.data['to_user'])
        friend_request = FriendshipRequest(from_user=from_user, to_user=to_user)
        friend_request.save()
        return Response(status=status.HTTP_201_CREATED)


class FriendshipAcceptView(generics.CreateAPIView):
    serializer_class = FriendshipRequestSerializer

    def post(self, request):
        return

