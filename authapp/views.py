from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect
from pytz import unicode
from rest_framework import viewsets, permissions, generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authapp.forms import GiftUserLoginForm, GiftUserRegisterForm, GiftUserEditForm
from django.contrib import auth
from django.urls import reverse
from django.conf import settings

from authapp.models import GiftUser
from authapp.permissions import IsOwnerOnly
from authapp.serializers import ProfileSerializer, AuthSerializer, ChangePasswordSerializer


def send_verify_mail(user):
    title = 'Подтверждение регистрации'
    verify_link = reverse('authapp:verify', args=[user.email, user.active_key])
    message = 'Для подтверждения на портале {domain_name} перейдите по ссылке {domain_name}{link}'\
        .format(domain_name = settings.DOMAIN_NAME, link = verify_link)
    from_address = 'djangolesson2019@yandex.ru'
    return send_mail(title, message, from_address, [user.email], fail_silently=False)


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = GiftUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            # if send_verify_mail(user):
            #     print('mail sent')
            # else:
            #     print('mail NOT sent')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = GiftUserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


def verify(request, email, activation_key):
    try:
        user = GiftUser.objects.get(email=email)
        if user.active_key == activation_key and not user.is_activation_key_expired():
            print(f'user {user} is activated')
            user.is_active = True
            user.save()
            auth.login(request, user)

            return render(request, 'authapp/verification.html')
        else:
            print(f'error activating user: {user}')
            return render(request, 'authapp/verification.html')

    except Exception as e:
        print(f'error activating user : {e.args}')

    return HttpResponseRedirect(reverse('main'))


#REST
class UserListView(generics.ListAPIView):
    queryset = GiftUser.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = GiftUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOnly, )


class LoginView(generics.CreateAPIView):
    serializer_class = AuthSerializer

    def get(self, request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            content = {'id': request.user.id,
                       'first_name': request.user.first_name,
                       }
            return Response(content, status=status.HTTP_200_OK)

    #Login
    def post(self, request, format=None):
        user = auth.authenticate(username=request.data['email'],
                                 password=request.data['password'])
        if user:
            content = {'name': user.first_name if False else user.email,
                       'id': user.id}

            if user.is_active:
                auth.login(request, user)
                return Response(content, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_403_FORBIDDEN)


class LogoutView(generics.RetrieveAPIView):
    def get(self, request):
        auth.logout(request)
        return Response(status=status.HTTP_200_OK)


class CreateUserView(generics.CreateAPIView):
    model = GiftUser
    permission_classes = (permissions.AllowAny, )
    serializer_class = AuthSerializer


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = GiftUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
