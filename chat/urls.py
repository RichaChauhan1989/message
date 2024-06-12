from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSet, MessageViewSet

router = DefaultRouter()
router.register('chatroom', ChatRoomViewSet, basename='chatroom')
router.register('Message', MessageViewSet, basename='Message')
urlpatterns = router.urls