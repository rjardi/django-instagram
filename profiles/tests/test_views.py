from django.test import TestCase
from django.urls import reverse
from profiles.models import UserProfile
from django.contrib.auth.models import User

class TestUserProfileViews(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(
            username="test",
            password="test",
            first_name="Risen",
            last_name="Jardí",
            email="danone@dana.com")
        self.profile =UserProfile.objects.create(user=self.user)

    def test_profile_list_views(self):
        self.client.login(username='test', password="test")
        url=reverse("profile_list")
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_views(self):
        self.client.login(username='test', password="test")
        url=reverse("profile_detail", args=[self.profile.pk])
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)
