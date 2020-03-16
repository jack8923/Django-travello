from django.test import TestCase
from django.contrib.auth.models import User, auth

# Create your tests here.
class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test1234', email='test@gmail.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = auth.authenticate(username='test', password='test1234')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_username(self):
        user = auth.authenticate(username='test1', password='test1234')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_password(self):
        user = auth.authenticate(username='test', password='test123')
        self.assertFalse(user is not None and user.is_authenticated)
