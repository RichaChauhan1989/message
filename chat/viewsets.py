from rest_framework import viewsets
from chat.models import ChatRoom
from chat.Serializers import ChatRoomSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
