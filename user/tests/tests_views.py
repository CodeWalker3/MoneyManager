import datetime
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import pytest

# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser", email="test")
        user.set_password("12345")
        user.save()
        self.clientV = Client()
        self.client.login(username="testuser", password="12345")


    def test_index_url(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_register_url(self):
        response = self.clientV.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.clientV.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_register_logged_url(self):
        response = self.client.get(reverse("register"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_logged_url(self):
        response = self.client.get(reverse("login"), follow=True)
        self.assertEqual(response.status_code, 200)

    
    def test_create_user(self):
        response = self.clientV.post(reverse("register"), data={
            'username':'testuser', 
            'email':'test@test.com',
            'password':'123456',
            'password1':'123456'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(reverse('register'))

    def test_create_wrong_user(self):
        response = self.clientV.post(reverse("register"), data={
            'username':'testusr', 
            'email':'test@test.cm',
            'password1':'1234'
        })
        self.assertEqual(response.status_code, 302)

    def test_user_none_post(self):
        response = self.clientV.post(reverse("login"), data={
            'username':'testuse', 
            'password':'12345'
        })
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        response = self.clientV.post(reverse("login"), data={
            'username':'testuser', 
            'password':'123456'
        })
        self.assertEqual(response.status_code, 200)

    
        
    def test_logout_url(self):
        response = self.client.get(reverse("signout"), follow=True)
        self.assertEqual(response.status_code, 200)


