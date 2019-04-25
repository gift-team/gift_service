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
from authapp.serializers import GiftUserSerializer


def send_verify_mail(user):
    title = 'Подтверждение регистрации'
    verify_link = reverse('authapp:verify', args=[user.email, user.active_key])
    message = 'Для подтверждения на портале {domain_name} перейдите по ссылке {domain_name}{link}'\
        .format(domain_name = settings.DOMAIN_NAME, link = verify_link)
    from_address = 'djangolesson2019@yandex.ru'
    return send_mail(title, message, from_address, [user.email], fail_silently=False)


def login(request):
    title = 'Вход'

    login_form = GiftUserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('authapp:edit'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('authapp:edit'))


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


@transaction.atomic
def edit(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = GiftUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = GiftUserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)


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
    serializer_class = GiftUserSerializer


class ProfileView(generics.RetrieveAPIView):
    queryset = GiftUser.objects.all()
    serializer_class = GiftUserSerializer


class LoginView(generics.RetrieveAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'email': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
            'message': 'congrats, youve authentificated',
        }
        if request.user.is_active:
            auth.login(request, request.user)
            return Response(content)

        return Response(status=status.HTTP_403_FORBIDDEN)


class LogoutView(generics.RetrieveAPIView):
    def get(self, request, format=None):
        auth.logout(request)
        return Response(status=status.HTTP_200_OK)


class CreateUserView(generics.CreateAPIView):
    model = GiftUser
    permission_classes = (permissions.AllowAny, )
    serializer_class = GiftUserSerializer
