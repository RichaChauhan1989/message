from rest_framework import viewsets
from chat.models import ChatRoom, Message
from chat.Serializers import ChatRoomSerializer, MessageSerializer



class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer