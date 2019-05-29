from django.urls import path
from giftapp.views import GiftsListView, CreateGiftView, GiftView

app_name = 'giftapp'

urlpatterns = [
    path('', GiftsListView.as_view()),
    path('create/', CreateGiftView.as_view()),
    path('view/<int:pk>/', GiftView.as_view()),
    # path('requests/accept/', FriendshipAcceptView.as_view()),
]
