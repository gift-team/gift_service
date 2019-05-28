import coreapi
import coreschema
from rest_framework import viewsets, permissions, generics, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema

from authapp.models import GiftUser
from friendsapp.permissions import IsOwnerOnly
from friendsapp.serializers import FriendsSerializer, FriendshipRequestSerializer
from friendsapp.models import Friends, FriendshipRequest
from gift_service import settings

from django.core import serializers

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class FriendsView(generics.RetrieveAPIView):
    serializer_class = FriendsSerializer

    def get(self, request):
        user = request.user
        qs = Friends.objects.select_related('from_user', 'to_user').filter(to_user=user).all()
        result = FriendsSerializer(qs, many=True).data
        return Response(result)


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
    schema = ManualSchema(fields=[
        coreapi.Field(
            name="id",
            required=True,
            location="form",
            schema=coreschema.Integer()
        )
    ])

    serializer_class = FriendshipRequestSerializer
    permission_classes = (IsOwnerOnly, )

    def post(self, request):
        object = FriendshipRequest.objects.get(id=request.data['id'], to_user=request.user)
        object.accept()
        return Response(status=status.HTTP_201_CREATED)

