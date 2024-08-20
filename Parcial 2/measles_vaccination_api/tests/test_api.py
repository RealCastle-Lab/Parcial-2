# tests/test_api.py
import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_all_vaccinations(self):
        response = self.client.get('/api/vaccinations')
        self.assertEqual(response.status_code, 200)
        self.assertIn('vaccination_data', response.json)

    def test_get_vaccination_by_year(self):
        response = self.client.get('/api/vaccinations/2020')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any('2020' in entry['Year'] for entry in response.json))

    def test_get_vaccination_by_year_not_found(self):
        response = self.client.get('/api/vaccinations/1999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
