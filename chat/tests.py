from django.test import TestCase
from rest_framework.test import APIClient
from .models import ChatRoom
from .serializers import ChatRoomSerializer

class ChatRoomViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.room1 = ChatRoom.objects.create(name='Room 1')
        self.room2 = ChatRoom.objects.create(name='Room 2')

    def test_list_chatrooms(self):
        # Test listing all chatrooms using GET request
        response = self.client.get('/api/chatrooms/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Assuming there are 2 chatrooms in the database

    def test_retrieve_chatroom(self):
        # Test retrieving a single chatroom using GET request
        url = '/api/chatrooms/{}/'.format(self.room1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Room 1')

    def test_create_chatroom(self):
        # Test creating a new chatroom using POST request
        data = {'name': 'New Room'}
        response = self.client.post('/api/chatrooms/', data)
        self.assertEqual(response.status_code, 201)  # 201 Created
        self.assertEqual(ChatRoom.objects.count(), 3)  # Check if a new chatroom was created

    def test_update_chatroom(self):
        # Test updating an existing chatroom using PUT request
        data = {'name': 'Updated Room Name'}
        url = '/api/chatrooms/{}/'.format(self.room1.id)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.room1.refresh_from_db()
        self.assertEqual(self.room1.name, 'Updated Room Name')

    def test_partial_update_chatroom(self):
        # Test partially updating an existing chatroom using PATCH request
        data = {'name': 'Partial Update'}
        url = '/api/chatrooms/{}/'.format(self.room1.id)
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.room1.refresh_from_db()
        self.assertEqual(self.room1.name, 'Partial Update')

    def test_delete_chatroom(self):
        # Test deleting an existing chatroom using DELETE request
        url = '/api/chatrooms/{}/'.format(self.room1.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)  # 204 No Content
        self.assertFalse(ChatRoom.objects.filter(id=self.room1.id).exists())
