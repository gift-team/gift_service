import rest_framework
from django.urls import include, path
from rest_framework import routers
from authapp import views, admin

import authapp.views as authapp

router = routers.DefaultRouter()
# router.register(r'users/', authapp.UserListView)
# router.register(r'users/<int:pk>', authapp.ProfileView)
# router.register(r'login', authapp.LoginView, base_name='login')

app_name = 'authapp'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('login/', authapp.login, name='login'),
    # path('logout/', authapp.logout, name='logout'),
    # path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    path('verify/<str:email>/<str:activation_key>', authapp.verify, name='verify'),

    path('login/', authapp.LoginView.as_view()),
    path('logout/', authapp.LogoutView.as_view()),
    path('register/', authapp.CreateUserView.as_view()),
    path('users/', authapp.UserListView.as_view()),
    path('users/<int:pk>/', authapp.ProfileView.as_view()),
    path('password/', authapp.ChangePasswordView.as_view()),

    path('rest/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
