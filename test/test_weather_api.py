import unittest
import json
from app import create_app, db
from models import User, FavoriteLocation

class WeatherApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_registration(self):
        response = self.client.post('/api/auth/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully!', str(response.data))

    def test_user_login(self):
        self.client.post('/api/auth/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        })
        response = self.client.post('/api/auth/login', json={
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)

    def test_add_favorite_location(self):
        self.client.post('/api/auth/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        })
        response = self.client.post('/api/auth/login', json={
            'username': 'testuser',
            'password': 'password'
        })
        token = response.json['token']
        response = self.client.post('/api/users/favorites', headers={'Authorization': f'Bearer {token}'}, json={
            'city': 'London',
            'country': 'UK'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Favorite location added successfully!', str(response.data))

    def test_get_current_weather(self):
        self.client.post('/api/auth/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        })
        response = self.client.post('/api/auth/login', json={
            'username': 'testuser',
            'password': 'password'
        })
        token = response.json['token']
        self.client.post('/api/users/favorites', headers={'Authorization': f'Bearer {token}'}, json={
            'city': 'London',
            'country': 'UK'
        })
        response = self.client.get('/api/weather/current', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()
