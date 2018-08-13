# -*- coding: utf-8 -*-
from .baseapi import BaseAPI

class Data(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.sn = None
        self.parameter = None
        self.unit = None
        self.timestamp = None
        self.timestamp_local = None
        self.last_updated = None
        self.value_1min = None
        self.value_15min = None
        self.value_30min = None
        self.value_60min = None

        super(Data, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, sn, id, **kwargs):
        pt = cls(token=token, sn=sn, id=id, **kwargs)

        pt.load()

        return pt

    def load(self):
        """"""
        data = self.fetch_data("device/{}/data/{}".format(self.sn, self.id))

        for key in data.keys():
            setattr(self, key, data[key])

        return data

    def destroy(self):
        """"""
        raise NotImplementedError("This feature is not yet implemented.")

    def update(self):
        """"""
        raise NotImplementedError("This feature is not yet implemented.")

    def __repr__(self):
        return str(self)
