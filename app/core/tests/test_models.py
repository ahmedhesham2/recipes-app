from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(email="ahmed_hesham99@outlook.com", password="admin")
        self.assertEqual(user.email, "ahmed_hesham99@outlook.com")  # add assertion here
        self.assertEqual(user.check_password("admin"), True)  # add assertion here

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(email="ahmed_hesham99@outlook.com", password="admin")
        self.assertTrue(user.is_staff)  # add assertion here
        self.assertTrue(user.is_superuser)  # add assertion here

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_normalize_email(self):
        email = "ahmed_hesham99@OUTLOOK.COM"
        password = "#@123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email.lower())  # add assertion here
