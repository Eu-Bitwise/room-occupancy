import unittest
import requests
from django.test import TestCase
import json

from occupancy_app.models import * 
from datetime import datetime

class HelloTest(TestCase):
    def test_test(self):
        self.assertEqual(1, 1)

class TestModel(TestCase):
    # Check PeopleCounter model
    def setUp(self):
        self.sensor_name = 'Sensor1'
        self.timestamp = datetime.now(),
        self.inside = 10
        self.out = 5

        self.people_counter = PeopleCounter.objects.create(
            sensor_name=self.sensor_name, timestamp=self.timestamp, inside=self.inside, out=self.out)

        def test_people_counter_model(self):
            sensor1 = PeopleCounter.objects.get(sensor_name=self.sensor_name)
            self.assertEqual(sensor1.timestamp, timestamp=self.timestamp)
            self.assertEqual(sensor1.inside, self.inside)
            self.assertEqual(sensor1.out, self.out)

class TestView(TestCase):
    # Check if the view occupancy
    def test_view_defined(self):
        response = self.client.get('/occupancy/')
        self.assertEqual(response.status_code, 200)

class TestTemplate(TestCase):
    # Check if the app html is rendered
    def test_template_render(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'occupancy.html')
        self.assertContains(response, '<title>Occupancy app</title>')

class TestApiEndpoint(TestCase):
    # Check if the api endpoint is reachable
    def test_api_endpoint(self):
        self.endpoint_url = 'http://localhost:8080/api/room-occupancy/'
        response = requests.get(self.endpoint_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.text))

if __name__ == '__main__':
    unittest.main()

