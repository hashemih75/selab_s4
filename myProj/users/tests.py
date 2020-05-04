from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from users.models import User


class ViewTestCase(TestCase):
    def test_signup_successful(self):
        old_users = User.objects.filter(username='sina')
        self.assertEqual(len(old_users), 0)
        response = self.client.post(reverse('signup'),
                                    {'username': 'sina', 'password1': 'S1D2D1D1Dcsdsa', 'password2': 'S1D2D1D1Dcsdsa',
                                     'email': 'sina@gmail.com',
                                     'birth_date': '1993-01-14'})
        self.assertEqual(response.status_code, 302)
        new_users = User.objects.filter(username='sina')
        self.assertEqual(len(new_users), 1)
