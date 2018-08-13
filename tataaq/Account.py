# -*- coding: utf-8 -*-

from .baseapi import BaseAPI

class Account(BaseAPI):
    """
    """
    def __init__(self, *args, **kwargs):
        self.email = None
        self.username = None
        self.confirmed = None

        super(Account, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, token=None, **kwargs):
        acct = cls(token=token, **kwargs)

        acct.load()

        return acct

    def load(self):
        """Load the user object from https://tatacenter-airquality.mit.edu/api/v1.0/account
        """
        data = self.fetch_data("account")

        for key in data.keys():
            setattr(self, key, data[key])

        return data
