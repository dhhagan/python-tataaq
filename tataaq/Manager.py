# -*- coding: utf-8 -*-
from .baseapi import BaseAPI
from .Account import Account
from .Device import Device

from .utils import list_to_dataframe

class Manager(BaseAPI):
    """
    """
    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)

    def get_account(self):
        """Return the account associated with the API key being used.
        """
        return Account.get_object(token=self.token)

    def get_devices(self, return_type='json', **kwargs):
        """Return a list of all devices either as objects or as a pandas DataFrame.
        """
        return_type = return_type.lower()
        if return_type not in ['json', 'dataframe', 'object']:
            return_type = 'json'

        data = self.fetch_data("device/", **kwargs)

        if return_type == 'dataframe':
            data = list_to_dataframe(data)
        if return_type == 'object':
            devs = list()
            for jsoned in data:
                dev = Device(**jsoned)
                dev.token = self.token

                devs.append(dev)

            data = devs

        return data

    def get_device(self, sn, return_type='json', **kwargs):
        """
        :param return_type: ['json', 'object']
        """
        data = self.fetch_data("device/{}".format(sn))

        return_type = return_type.lower()
        if return_type not in ['json', 'object']:
            raise TypeError("return_type must be either json or object.")

        if return_type == 'object':
            obj = Device(**data)
            obj.token = self.token

            return obj

        return data

    def post_device(self, data, **kwargs):
        """"""
        raise NotImplementedError("This method is not yet implemented.")

    def delete_device(self, sn, **kwargs):
        """DELETE a device forever. """
        raise NotImplementedError("This method is not yet implemented.")
