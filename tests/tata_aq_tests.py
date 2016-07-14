import unittest
import TataAQ
import pandas as pd

class SetupTestCase(unittest.TestCase):
    def setUp(self):
        self.test_key = '2JIUSQNEJM1N8M44NALA6JA4'
        self.api = TataAQ.TataAQ(self.test_key)

    def tearDown(self):
        pass

    def test_setup(self):
        self.assertIsInstance(self.api, TataAQ.TataAQ)

    def test_make_url(self):
        self.assertEqual(self.api._make_url('auth/'), "https://tatacenter-airquality.mit.edu/api/v2.0/auth/")

    def test_ping(self):
        status, resp = self.api.ping()

        self.assertEqual(status, 200)

    def test_ebam_data(self):
        status, resp = self.api.ebam()

        self.assertEqual(status, 200)

    def test_ebam_with_params(self):
        params = {
            'expand': 1,
            'per_page': 100
        }

        status, resp = self.api.ebam(params = params)

        self.assertEqual(status, 200)
        self.assertTrue(type(resp['data'][0]) != str)
        self.assertEqual(resp['meta']['per_page'], 100)

    def test_ebam_data_page_number(self):
        params = {
            'expand': 1,
            'per_page': 10,
            'page': 3
        }

        status, resp = self.api.ebam(params = params)

        self.assertEqual(status, 200)
        self.assertEqual(resp['meta']['page'], 3)
