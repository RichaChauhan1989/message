from rest_framework import serializers
from chat.models import ChatRoom,Message



class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text','user','chat_room']