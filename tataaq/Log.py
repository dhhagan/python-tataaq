# -*- coding: utf-8 -*-
from .baseapi import BaseAPI

class Log(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.url = None
        self.sn = None
        self.opened = None
        self.closed = None
        self.message = None
        self.adressed = None
        self.level = None

        super(Log, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, id, token=None, **kwargs):
        log = cls(token=token, id=id, **kwargs)

        log.load()

        return log

    def load(self):
        """"""
        data = self.fetch_data("log/{}".format(self.id))

        for key in data.keys():
            setattr(self, key, data[key])

        return data

    def destroy(self):
        """"""
        raise NotImplementedError("This feature is not yet implemented.")

    def close(self):
        """"""
        raise NotImplementedError("This feature is not yet implemented.")

    def __repr__(self):
        return str(self)
