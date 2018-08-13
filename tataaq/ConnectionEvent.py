# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, PUT, DELETE, POST, GET
from .utils import list_to_dataframe

class ConnectionEvent(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.millis = None
        self.sn = None
        self.timestamp = None
        self.msg = None

        super(ConnectionEvent, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, sn, token=None):
        event = cls(token=token, sn=sn)

        event.load()

        return event

    def load(self):
        """"""
        data = self.fetch_data("connection_event/{}".format(self.sn))

        for key in data.keys():
            setattr(self, key, data[key])

        return data

    def destroy(self):
        """"""
        raise NotImplementedError("This feature is not yet implemented.")

    def __repr__(self):
        return str(self)
