from django.urls import path
from giftapp.views import CreateGiftView

from rest_framework.routers import DefaultRouter

app_name = 'giftapp'

# from api.orders.views import OrderViewSet, OrderItemViewSet, OrderReturnViewSet

router = DefaultRouter()

router.register(r'', CreateGiftView, basename='gifts')

urlpatterns = router.urls

# urlpatterns = [
#     path('create/', CreateGiftView.as_view()),
#     # path('requests/accept/', FriendshipAcceptView.as_view()),
# ]
