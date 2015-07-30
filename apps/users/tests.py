from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.factories import UserFactory, UserCountryFactory


class UserTests(APITestCase):

    def test_empty_user_list(self):
        """
        Test the user list
        """
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_user_list(self):
        """
        Test the user list
        """
        url = reverse('user-list')
        users = UserFactory.create_batch(4)
        UserCountryFactory.create_batch(15, user=users[0])

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 4)
