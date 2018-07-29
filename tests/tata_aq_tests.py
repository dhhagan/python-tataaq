"""Unittests."""
import unittest
import tataaq
import pandas as pd
from tataaq.exceptions import TataRequestError, RequestKeywordError

device_sn = "TREX001"


class SetupTestCase(unittest.TestCase):
    """Run the unittests."""
    def setUp(self):
        self.api = tataaq.Api()

    def tearDown(self):
        pass
        

    """
    def setUp(self):
        self.test_key = '2JIUSQNEJM1N8M44NALA6JA4'
        self.api = tataaq.TataAQ(apikey=self.test_key)

    def tearDown(self):
        pass

    def test_setup(self):
        self.assertIsInstance(self.api, tataaq.TataAQ)

    def test_makebaseurl(self):
        url = "https://tatacenter-airquality.mit.edu/api/v1.0/auth/"
        self.assertEqual(self.api._makebaseurl('auth/'), url)

    def test_basic_get_request(self):
        resp = self.api._get('auth/')

        url = "https://tatacenter-airquality.mit.edu/api/v1.0/auth/"

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.url, url)

    def test_invalid_request_method(self):
        with self.assertRaises(RequestError):
            self.api._send('auth/', 'UPDATE')

    def test_ping(self):
        resp = self.api.ping()

        self.assertEqual(resp.status_code, 200)

    def test_get_devices(self):
        resp = self.api.device()

        url = "https://tatacenter-airquality.mit.edu/api/v1.0/device/"

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.url, url)

    def test_get_device_with_keywords(self):
        resp = self.api.device(per_page=2)

        data = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['meta']['per_page'], 2)

        resp = self.api.device(filter="city,eq,Hilo")

        self.assertEqual(resp.status_code, 200)
        for each in resp.json()['data']:
            self.assertEqual(each['city'], 'Hilo')

    def test_get_ind_device(self):
        resp = self.api.device(sn=device_sn)
        url = "https://tatacenter-airquality.mit.edu/" + \
              "api/v1.0/device/{}".format(device_sn)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.url, url)

    def test_device_data(self):
        resp = self.api.data(sn=device_sn)

        self.assertEqual(resp.status_code, 200)

    def test_error_with_required_kw(self):
        with self.assertRaises(KeywordError):
            resp = self.api.data()

    def test_dataframes(self):
        meta, resp = self.api.data(sn=device_sn, dataframe=True)

        self.assertIsInstance(resp, pd.DataFrame)
        self.assertIsNotNone(meta['page'])
        self.assertIsNotNone(meta['pages'])
        self.assertIsNotNone(meta['next_url'])
        self.assertIsNotNone(meta['first_url'])
        self.assertIsNotNone(meta['last_url'])
        self.assertIsNotNone(meta['per_page'])
        self.assertIsNotNone(meta['total'])
    """
