from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import UserProfile, Follow

class UserProfileModelTest(TestCase):
    def setUp(self):
        # print('Ejecutando setUp')
        # Crear usuarios y sus perfiles
        self.user1=User.objects.create_user(
            username="John",
            email="john@lennon.com",
            password="password123"
        )

        self.user2=User.objects.create_user(
            username="Paul",
            email="paul@mccartney.com",
            password="password123"
        )
        self.profile1=UserProfile.objects.create(
            user=self.user1,
            bio="I'm a rock star",
            birth_date="1940-10-09"
        )
        self.profile2=UserProfile.objects.create(
            user=self.user2,
            bio="I'm a rock star too",
            birth_date="1942-06-18"
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.profile1.bio, "I'm a rock star")
        self.assertEqual(self.user1.username, "John")

    def test_follow_user(self):
        self.profile1.follow(self.profile2)
        self.assertTrue(Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())

    def test_unfollow_user(self):
        self.profile1.follow(self.profile2)
        self.assertTrue(Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())
        self.profile1.unfollow(self.profile2)
        self.assertFalse(Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())

    def test_str_userprofile(self):
        self.assertEqual(str(self.profile1),self.profile1.user.username)

    def test_unique_follow_once_time(self):
        Follow.objects.get_or_create(follower=self.profile1, following=self.profile2)
        self.assertEqual(Follow.objects.filter(follower=self.profile1, following=self.profile2).count(),1)
        Follow.objects.get_or_create(follower=self.profile2, following=self.profile2)
        self.assertEqual(Follow.objects.filter(follower=self.profile1, following=self.profile2).count(),1)
