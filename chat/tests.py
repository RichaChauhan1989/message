from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ChatRoom
from .Serializers import ChatRoomSerializer
from django.urls import reverse


class ChatRoomViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.room1 = ChatRoom.objects.create(name='Room 1')
        self.room2 = ChatRoom.objects.create(name='Room 2')
        self.valid_payload = {
            'name': 'New Room'
        }
        self.invalid_payload = {
            'name': ''
        }

    def test_list_chatrooms(self):
        response = self.client.get(reverse('chatroom-list'))
        chatrooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_chatroom(self):
        response = self.client.get(reverse('chatroom-detail', kwargs={'pk': self.room1.pk}))
        chatroom = ChatRoom.objects.get(pk=self.room1.pk)
        serializer = ChatRoomSerializer(chatroom)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_chatroom(self):
        response = self.client.post(reverse('chatroom-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatRoom.objects.count(), 3)

    def test_create_invalid_chatroom(self):
        response = self.client.post(reverse('chatroom-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ChatRoom.objects.count(), 2)

    def test_update_chatroom(self):
        response = self.client.put(
            reverse('chatroom-detail', kwargs={'pk': self.room1.pk}),
            data={'name': 'Updated Room Name'},
            format='json'
        )
        self.room1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.room1.name, 'Updated Room Name')

    def test_partial_update_chatroom(self):
        response = self.client.patch(
            reverse('chatroom-detail', kwargs={'pk': self.room1.pk}),
            data={'name': 'Partial Update'},
            format='json'
        )
        self.room1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.room1.name, 'Partial Update')

    def test_delete_chatroom(self):
        response = self.client.delete(reverse('chatroom-detail', kwargs={'pk': self.room1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ChatRoom.objects.filter(pk=self.room1.pk).exists())
