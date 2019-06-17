from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Tutor
from ..serializers import TutorSerializer


class TutorsViewTestCase(APITestCase):

    def setUp(self):
        Tutor.objects.all().delete()
        self.tutor_data = {'name': 'Bob',
                           'subject': 'art',
                           'description': 'super tutor'}
        self.response = self.client.post(reverse('tutor-list'), self.tutor_data, format="json")

    def test_create_tutor(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.data['name'], self.tutor_data['name'])

    def test_create_invalid_tutor(self):
        """ this can be expended to test each param """

        tutor_data = {
            'name': ''.join(('s' for i in range(0, 300))),
            'description': 'super tutor',
            'subject': 'some subject'
        }
        response = self.client.post(reverse('tutor-list'), tutor_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_tutors(self):
        response = self.client.get(reverse('tutor-list'), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(self.response.data) > 0)

    def test_get_tutor(self):
        tutor = Tutor.objects.get(pk=1)

        response = self.client.get(reverse('tutor-detail', kwargs={'pk': 1}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.data['name'], tutor.name)

    def test_update_tutor(self):
        tutor = Tutor.objects.get(pk=1)
        tutor.description = 'i\'m the tutor'

        serializer = TutorSerializer(tutor)

        response = self.client.put(reverse('tutor-detail', kwargs={'pk': 1}), serializer.data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], tutor.description)

    def test_edit_tutor(self):
        description = 'i\'m the tutor'
        response = self.client.patch(reverse('tutor-detail', kwargs={'pk': 1}),
                                     {'description': description},
                                     format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], description)

    def test_delete_tutor(self):
        response = self.client.delete(reverse('tutor-detail', kwargs={'pk': 1}), format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)