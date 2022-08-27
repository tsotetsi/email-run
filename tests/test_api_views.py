from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .factories import UserFactory


class UserModelTests(APITestCase):

    def setUp(self) -> None:
        super(UserModelTests, self).setUp()
        self.client = APIClient()
        self.user = UserFactory()

    def test_user_view_set_list(self):
        """
        Ensure admin can retrieve all users.
        """
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
