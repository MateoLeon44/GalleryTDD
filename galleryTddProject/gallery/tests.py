from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.http import JsonResponse

# Create your tests here.
from .models import Image
import json

# Create your tests here.


class GalleryTestCase(TestCase):

    def test_list_images_status(self):
        url = '/gallery/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_verify_first_from_images_list(self):
        user_model = User.objects.create_user(
            username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(
            name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(
            name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response = self.client.get('/gallery/')
        current_data = json.loads(response.content)

        self.assertEqual(current_data[0]['fields']['name'], "nuevo")

    def test_add_user(self):
        response = self.client.post('/gallery/addUser/', json.dumps({"username": "testUser", "first_name": "Test",
                                                                     "last_name": "User", "password": "AnyPas#5", "email": "test@test.com"}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'], 'testUser')

    def test_list_portflio(self):
        user_model = User.objects.create_user(
            username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(
            name='test', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(
            name='test1', url='No', description='testImage', type='jpg', user=user_model)

        response = self.client.get('/gallery/3/portfolio')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['name'], 'test')

    def test_count_images_list(self):
        user_model = User.objects.create_user(
            username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(
            name='test', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(
            name='test1', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(
            name='test2', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(
            name='test3', url='No', description='testImage', type='jpg', user=user_model)
        response = self.client.get('/gallery/')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 4)

    def login(self):
        user_model = User.objects.create_user(
            username='testUser', password='kd8wke-DE34', first_name='Test', last_name='Test', email='test@test.com')
        response = self.client.post('/gallery/login/', json.dumps(
            {"username": "testUser", "password": "kd8wke-DE34"}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_list_portflio_public(self):
        user_model = User.objects.create_user(
            username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(
            name='test', url='No', description='testImage', type='jpg', user=user_model, public=True)
        Image.objects.create(
            name='test1', url='No', description='testImage', type='jpg', user=user_model, public=False)

        response = self.client.get('/gallery/4/portfolio')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['name'], 'test')

