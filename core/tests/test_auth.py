import imp
from django.test import TestCase
from core import models
from django.contrib.auth import get_user_model

class TestAuth(TestCase):
    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser('teste@test.com', 'pass123')
        self.assertTrue(user.is_superuser)
