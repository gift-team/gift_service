from django.urls import include, path
import authapp.views as authapp


app_name = 'authapp'

urlpatterns = [
    # path('verify/<str:email>/<str:activation_key>', authapp.verify, name='verify'),

    path('login/', authapp.LoginView.as_view()),
    path('logout/', authapp.LogoutView.as_view()),
    path('register/', authapp.CreateUserView.as_view()),
    path('users/', authapp.UserListView.as_view()),
    path('users/<int:pk>/', authapp.ProfileView.as_view()),
    path('password/', authapp.ChangePasswordView.as_view()),

    path('rest/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
