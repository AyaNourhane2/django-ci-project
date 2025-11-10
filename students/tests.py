from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Student

class StudentTests(APITestCase):
    
    def test_create_student(self):
        url = reverse('add_student')
        data = {'name': 'John', 'address': 'Algeria'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.count(), 1)
    
    def test_get_all_students(self):
        Student.objects.create(name='Charlie', address='Algeria')
        url = reverse('get_all_students')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)