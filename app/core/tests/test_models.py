from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTeasts(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successfull"""
        email = "test@schadrack.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test for new user is normalized"""
        email = 'test@SCHADRACK.com'
        user = get_user_model().objects.create_user(email, 'Test123')
        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@schadrack.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
