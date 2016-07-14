import json
import requests
import pandas as pd

from pkg_resources import get_distribution

#__all__ = ['TataAQ']

__version__ = get_distribution('py-openaq').version

class API(object):
    """Generic API Base Wrapper
    """
    def __init__(self, **kwargs):
        self._username  = kwargs.pop('username', '')
        self._password  = kwargs.pop('password', '')
        self._version   = kwargs.pop('version', '')
        self._baseurl   = kwargs.pop('baseurl', '')
        self._headers   = {'content-type': 'application/json'}

    def _make_url(self, endpoint):
        """Internal method to create a url from an endpoint

            :param endpoint: Endpoint for an API call

            :returns: url
        """
        return "{}/{}/{}".format(self._baseurl, self._version, endpoint)

class TataAQ(API):
    """
    """
    def __init__(self, version = 'v2', **kwargs):
        self._baseurl = 'https://tatacenter-airquality.mit.edu/api'

        super(TataAQ, self).__init__(version = version, baseurl = self._baseurl)
