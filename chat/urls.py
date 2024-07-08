from django.urls import path
from rest_framework.routers import DefaultRouter

from chat.views import sumNumbersView
from chat.viewsets import ChatRoomViewSet, MessageViewSet

router = DefaultRouter()
router.register('chatroom', ChatRoomViewSet, basename='chatroom')
router.register('Message', MessageViewSet, basename='Message')
urlpatterns = router.urls
urlpatterns += [
    path('sum_numbers/', sumNumbersView, name='sum_numbers'),
]