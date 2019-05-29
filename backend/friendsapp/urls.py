from django.urls import path
from friendsapp.views import FriendsView, FriendshipRequestView, FriendshipAcceptView

app_name = 'friendsapp'

urlpatterns = [
    path('', FriendsView.as_view()),
    path('requests/', FriendshipRequestView.as_view()),
    path('requests/accept/', FriendshipAcceptView.as_view()),
]
