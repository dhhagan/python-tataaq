"""Unittests."""
import unittest
import tataaq
import pandas as pd
import os
import sys

device_sn = "TREX001"


class SetupTestCase(unittest.TestCase):
    """Run the unittests."""
    def setUp(self):
        self.token = os.environ.get("TATAAQ_TOKEN_DEV")
        self.api = tataaq.Manager(token=self.token)

        if sys.platform == 'darwin': # if on local machine, change to local server for testing
            self.api.endpoint = "http://localhost:5000/api/v1.0/"

    def tearDown(self):
        pass

    def test_manager(self):
        # make sure
        self.assertIsInstance(self.api, tataaq.Manager)
        self.assertTrue(hasattr(self.api, 'get_account'))
        self.assertTrue(hasattr(self.api, 'get_devices'))
        self.assertTrue(hasattr(self.api, 'get_device'))
        self.assertTrue(hasattr(self.api, 'post_device'))
        self.assertTrue(hasattr(self.api, 'delete_device'))

        # .post_device(data)
        with self.assertRaises(NotImplementedError):
            self.api.post_device({})

        # .delete_device(sn)
        with self.assertRaises(NotImplementedError):
            self.api.delete_device(sn='TEST')

        # .get_account()
        if sys.platform != 'darwin':
            acct = self.api.get_account()
            self.assertIsInstance(acct, tataaq.Account)
            self.assertIsNotNone(acct.email)
            self.assertIsNotNone(acct.username)

        # .get_devices()
        devs = self.api.get_devices(return_type='json')

        dev1 = devs[0]

        devs = self.api.get_devices(return_type='dataframe')
        self.assertIsInstance(devs, pd.DataFrame)

        devs = self.api.get_devices(return_type='object')
        for dev in devs:
            self.assertIsInstance(dev, tataaq.Device)

        devs = self.api.get_devices(return_type='jsonz')
        self.assertTrue(type(devs) is list)

        # .get_device(sn)
        dev = self.api.get_device(sn=dev1['sn'], return_type='json')
        self.assertIsNotNone(dev['sn'])

        dev = self.api.get_device(sn=dev1['sn'], return_type='object')
        self.assertIsInstance(dev, tataaq.Device)

        with self.assertRaises(TypeError):
            self.api.get_device(sn=dev1['sn'], return_type='garbage')

    def test_account(self):
        acct = tataaq.Account.get_object(token=self.token, endpoint=self.api.endpoint)

        self.assertTrue(hasattr(acct, 'get_object'))
        self.assertTrue(hasattr(acct, 'load'))

    def test_connection_events(self):
        devs = self.api.get_devices(return_type='object')
        dev = devs[0]

        if sys.platform == 'darwin':
            dev.endpoint = self.api.endpoint # stupid laptop shit

        events = dev.get_connection_events(return_type='object')

        if len(events) > 0:
            event = events[0]

            self.assertIsInstance(event, tataaq.ConnectionEvent)

    def test_device(self):
        devs = self.api.get_devices(return_type='object')

        dev = tataaq.Device.get_object(sn=devs[0].sn, token=self.api.token, endpoint=self.api.endpoint)

        # Device()
        self.assertIsInstance(dev, tataaq.Device)

        # .destroy()
        with self.assertRaises(NotImplementedError):
            dev.destroy()

        # .update(data=dict())
        city = dev.city
        dev = dev.update(data=dict(city='tmp'))
        self.assertEqual(dev.city, "tmp")
        dev = dev.update(data=dict(city=city))
        self.assertEqual(dev.city, city)

        # .get_data()
        data = dev.get_data(return_type='json')

        data = dev.get_data(return_type='dataframe')
        self.assertIsInstance(data, pd.DataFrame)

        data = dev.get_data(return_type='object', params=dict(limit=10))

        data = dev.get_data(return_type='garbage', params=dict(limit=10))

        # .get_raw_data()
        data = dev.get_raw_data(return_type='json', params=dict(filter="timestamp,gt,2018-08-01"))
        self.assertTrue(type(data), list)

        data = dev.get_raw_data(return_type='dataframe', params=dict(filter="timestamp,gt,2018-08-01"))
        self.assertIsInstance(data, pd.DataFrame)

        data = dev.get_raw_data(return_type='object', params=dict(filter="timestamp,gt,2018-08-01"))
        self.assertTrue(type(data), list)

        data = dev.get_raw_data(return_type='garbage', params=dict(filter="timestamp,gt,2018-08-01"))
        self.assertTrue(type(data), list)

        # .get_logs()
        logs = dev.get_logs(return_type='json')
        self.assertTrue(type(logs), list)

        logs = dev.get_logs(return_type='dataframe')
        self.assertIsInstance(logs, pd.DataFrame)

        logs = dev.get_logs(return_type='object')
        for log in logs:
            self.assertIsInstance(log, tataaq.Log)

        logs = dev.get_logs(return_type='jsonz')
        self.assertTrue(type(logs), list)

        # .get_log()
        with self.assertRaises(NotImplementedError):
            dev.get_log()

        # .get_connection_events()
        events = dev.get_connection_events(return_type='json')
        self.assertTrue(type(events), list)

        events = dev.get_connection_events(return_type='dataframe')
        self.assertIsInstance(events, pd.DataFrame)

        events = dev.get_connection_events(return_type='object')
        for event in events:
            self.assertIsInstance(event, tataaq.ConnectionEvent)

        events = dev.get_connection_events(return_type='jsonz')
        self.assertTrue(type(events), list)

        # .get_latest()
        with self.assertRaises(NotImplementedError):
            dev.get_latest()

    def test_log(self):
        devs = self.api.get_devices(return_type='object')

        log = tataaq.Log.get_object(token=self.api.token, endpoint=self.api.endpoint, id=1)
        self.assertIsInstance(log, tataaq.Log)

        with self.assertRaises(NotImplementedError):
            log.close()

    def test_data(self):
        devs = self.api.get_devices(return_type='object')
        dev = devs[0]

        dev.endpoint = self.api.endpoint

        data = dev.get_data()

        if len(data) > 0:
            data = data[0]
            data = tataaq.Data.get_object(sn=dev['sn'], id=data['id'], token=self.api.token, endpoint=self.api.endpoint)

            self.assertIsInstance(data, tataaq.Data)
