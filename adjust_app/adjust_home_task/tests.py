import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .models import PerformanceMetrics

class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_general_case(self):
        PerformanceMetrics.objects.create(id=1, date="2017-05-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="DE", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=3, date="2017-05-17", channel="chartboost", country="DE", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=date.lt:2017-06-01&fields=impressions,clicks&group_by=channel,country&sort_by=clicks:desc",
            format="json")
        expected = [
            {'impressions': 2, 'clicks': 2, 'channel': 'chartboost', 'country': 'DE'},
            {'impressions': 1, 'clicks': 1, 'channel': 'adcolony', 'country': 'US'}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def test_records_are_sorted_correctly_in_descending_order(self):
        PerformanceMetrics.objects.create(id=1, date="2017-05-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=date.lt:2017-06-01&fields=impressions,clicks,channel&sort_by=channel:desc",
            format="json")
        expected = [
            {'impressions': 1, 'clicks': 1, 'channel': 'chartboost'},
            {'impressions': 1, 'clicks': 1, 'channel': 'adcolony'}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def test_records_are_sorted_correctly_in_ascending_order(self):
        PerformanceMetrics.objects.create(id=1, date="2017-05-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=date.lt:2017-06-01&fields=impressions,clicks,channel&sort_by=channel:asc",
            format="json")
        expected = [
            {'impressions': 1, 'clicks': 1, 'channel': 'adcolony'},
            {'impressions': 1, 'clicks': 1, 'channel': 'chartboost'}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def  test_that_records_are_sorted_by_default_in_ascending_order(self):
        PerformanceMetrics.objects.create(id=1, date="2017-05-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=date.lt:2017-06-01&fields=impressions,clicks,channel&sort_by=channel",
            format="json")
        expected = [
            {'impressions': 1, 'clicks': 1, 'channel': 'adcolony'},
            {'impressions': 1, 'clicks': 1, 'channel': 'chartboost'}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def test_if_fields_are_extracted_correctly_as_per_input(self):
        PerformanceMetrics.objects.create(id=1, date="2017-05-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=date.lt:2017-06-01&fields=impressions,clicks",
            format="json")
        expected = [
            {'impressions': 1, 'clicks': 1},
            {'impressions': 1, 'clicks': 1}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def test_if_fields_are_correctly_aggregated_upon_group_by(self):
        PerformanceMetrics.objects.create(id=1, date="2017-05-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=date.lt:2017-06-01&fields=impressions,clicks&group_by=country",
            format="json")
        expected = [
            {'impressions': 2, 'clicks': 2, 'country': 'US'}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def test_if_cpi_is_correctly_computed_upon_group_by(self):
        PerformanceMetrics.objects.create(id=1, date="2017-05-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=date.lt:2017-06-01&fields=impressions,clicks,cpi&group_by=country",
            format="json")
        expected = [
            {'impressions': 2, 'clicks': 2, 'country': 'US', 'cpi': 1}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def test_if_cpi_is_correctly_computed_without_group_by(self):
        PerformanceMetrics.objects.create(id=1, date="2017-05-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=date.lt:2017-06-01&fields=impressions,clicks,cpi",
            format="json")
        expected = [
            {'impressions': 1, 'clicks': 1, 'cpi': 1},
            {'impressions': 1, 'clicks': 1, 'cpi': 1}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def test_for_date_ranges(self):
        PerformanceMetrics.objects.create(id=1, date="2017-06-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=date.gte:2017-06-01,date.lte:2017-06-31&fields=impressions,clicks,channel",
            format="json")
        expected = [
            {'impressions': 1, 'clicks': 1, 'channel': 'adcolony'}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def test_that_api_returns_all_fields(self):
        PerformanceMetrics.objects.create(id=1, date="2017-06-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?q=country:US",
            format="json")
        expected = [
            {'id':1, 'date':"2017-06-17", 'channel':"adcolony", 'country':"US", 'impressions':1, 'clicks':1, 'installs':1, 'spend':1, 'revenue':1, 'operating_system':"android"}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)

    def test_that_all_rows_returned_when_no_filters_are_provided(self):
        PerformanceMetrics.objects.create(id=1, date="2017-06-17", channel="adcolony", country="US", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")
        PerformanceMetrics.objects.create(id=2, date="2017-05-17", channel="chartboost", country="DE", impressions=1, clicks=1, installs=1, spend=1, revenue=1, operating_system="android")

        response = self.client.get(
            path="/get-data?fields=channel,clicks,impressions,country",
            format="json")
        expected = [
            {'channel':"adcolony", 'impressions':1, 'clicks':1, 'country': 'US'},
            {'channel':"chartboost", 'impressions':1, 'clicks':1, 'country': 'DE'}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected)
