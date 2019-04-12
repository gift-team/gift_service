from django.urls import include, path
from rest_framework import routers
# from authapp import views

import authapp.views as authapp

router = routers.DefaultRouter()
router.register(r'users', authapp.UserViewSet)

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    path('verify/<str:email>/<str:activation_key>', authapp.verify, name='verify'),

    path('rest/', include(router.urls)),
    path('rest/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
