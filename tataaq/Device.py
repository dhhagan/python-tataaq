# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, PUT, DELETE, POST, GET
from .Data import Data
from .Log import Log
from .ConnectionEvent import ConnectionEvent

from .utils import list_to_dataframe

class Device(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.sn = None
        self.city = None
        self.country = None
        self.last_updated = None
        self.latitude = None
        self.longitude = None
        self.model = None
        self.outdoors = None
        self.timezone = None
        self.url = None

        super(Device, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, sn, token=None, **kwargs):
        dev = cls(token=token, sn=sn, **kwargs)

        dev.load()

        return dev

    def load(self):
        """"""
        data = self.fetch_data("device/{}".format(self.sn))

        for key in data.keys():
            setattr(self, key, data[key])

        return data

    def destroy(self):
        """"""
        raise NotImplementedError("This feature is not yet implemented.")

    def update(self, data, **kwargs):
        """data must be a dict
        """
        data = self.fetch_data("device/{}".format(self.sn), params=data, type=PUT)

        # update with new params
        for k, v in data.items():
            setattr(self, k, v)

        return self

    def get_data(self, return_type='json', **kwargs):
        """Return data for a device - pulls from a sanitized data table which contains
        1min, 15min, 30min, and 1h averaged data."""
        return_type = return_type.lower()
        if return_type not in ['json', 'dataframe', 'object']:
            return_type = 'json'

        data = self.fetch_data("device/{}/data/".format(self.sn), **kwargs)

        if return_type == 'dataframe':
            data = list_to_dataframe(data)
        if return_type == 'object':
            dataz = list()
            for jsoned in data:
                pt = Data(**jsoned)
                pt.token = token

                dataz.append(pt)

            data = dataz

        return data

    def get_raw_data(self, return_type='json', **kwargs):
        """Return data for a device - pulls from the raw datatable"""
        return_type = return_type.lower()
        if return_type not in ['json', 'dataframe']:
            return_type = 'json'

        data = self.fetch_data("researcher/device/{}/data/".format(self.sn), **kwargs)

        if return_type == 'dataframe':
            data = list_to_dataframe(data)

        return data

    def get_logs(self, return_type='json', **kwargs):
        """Return the logs for a specific device. Can be returned either as objects, in json format
        or as a dataframe
        """
        return_type = return_type.lower()
        if return_type not in ['json', 'dataframe', 'object']:
            return_type = 'json'

        data = self.fetch_data("log/{}".format(self.sn), **kwargs)

        if return_type == 'dataframe':
            data = list_to_dataframe(data)
        if return_type == 'object':
            logs = list()
            for jsoned in data:
                log = Log(**jsoned)
                log.token = self.token

                logs.append(log)

            data = logs

        return data

    def get_log(self, return_type='json', **kwargs):
        """"""
        raise NotImplementedError("This method is not yet implemented.")

    def get_connection_events(self, return_type='json', **kwargs):
        """Return a list of connection events for the device. Can be returned as either
        json format, a dataframe, or a list of objects.
        """
        return_type = return_type.lower()
        if return_type not in ['json', 'dataframe', 'object']:
            return_type = 'json'

        data = self.fetch_data("connection_event/{}".format(self.sn), **kwargs)

        if return_type == 'dataframe':
            data = list_to_dataframe(data)
        if return_type == 'object':
            events = list()
            for jsoned in data:
                connEvent = ConnectionEvent(**jsoned)
                connEvent.token = self.token

                events.append(connEvent)

            data = events

        return data

    def get_latest(self, **kwargs):
        """"""
        raise NotImplementedError("Not yet implemented.")

    def __repr__(self):
        return "<Device %s>" % self.sn
