from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .models import PerformanceMetrics

client = Client()

class TestApi(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_case_one(self):
        response = self.client.get(
            path="http://127.0.0.1:8000/get-data?q=date.lt:2017-06-01&fields=impressions,clicks&group_by=channel,country&sort_by=clicks:desc",
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_case_two(self):
        response = self.client.get(
            path="http://127.0.0.1:8000/get-data?q=date.gte:2017-05-01,date.lte:2017-05-31,operating_system:ios&fields=installs&group_by=date&sort_by=date",
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_case_three(self):
        response = self.client.get(
            path="http://127.0.0.1:8000/get-data?q=date:2017-06-01,country:US&fields=revenue&group_by=operating_system&sort_by=revenue:desc",
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_case_four(self):
        response = self.client.get(
            path="http://127.0.0.1:8000/get-data?q=country:CA&fields=cpi,spend&group_by=channel&sort_by=cpi:desc",
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
