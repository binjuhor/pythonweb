from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls.base import resolve

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_result(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)