from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect
from pytz import unicode
from rest_framework import viewsets, permissions, generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from authapp.forms import GiftUserLoginForm, GiftUserRegisterForm, GiftUserEditForm
from django.contrib import auth
from django.urls import reverse
from django.conf import settings

from authapp.models import GiftUser
from giftapp.models import Gift
# from authapp.permissions import IsOwnerOnly
from authapp.serializers import ProfileSerializer, AuthSerializer, ChangePasswordSerializer, AddressListSerializer
from giftapp.serializers import GiftSerializer, CreateGiftSerializer

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your views here.


# REST
class CreateGiftView(generics.CreateAPIView):
    model = Gift
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CreateGiftSerializer

    def post(self, request):
        user = request.user
        if user:
            content = {'owner': user.id}

            if user.is_active:
                return Response(content, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_403_FORBIDDEN)


class GiftsListView(generics.ListAPIView):

    queryset = Gift.objects.all().order_by('owner', 'name', )
    serializer_class = GiftSerializer


class GiftView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self, request):
        return Gift.objects.get(id=self.kwargs['pk'])
    serializer_class = GiftSerializer

