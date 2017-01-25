import json
import requests
import pandas as pd

from .exceptions import RequestError
from .decorators import requires_kws, makedataframe

from pkg_resources import get_distribution

__all__ = ['TataAQ']

__version__ = get_distribution('tataaq').version

class API(object):
    """Generic API Base Wrapper
    """
    def __init__(self, **kwargs):
        self._apikey    = kwargs.pop('apikey', '')
        self._secret    = kwargs.pop('secret', '')
        self._version   = kwargs.pop('version', '')
        self._baseurl   = kwargs.pop('baseurl', '')
        self._headers   = {'content-type': 'application/json'}

        self._auth      = (self._apikey, self._secret)

    def _makebaseurl(self, endpoint):
        """Internal method to create a url from an endpoint

            :param endpoint: Endpoint for an API call

            :type endpoint: string

            :returns: url
        """
        return "{}/{}/{}".format(self._baseurl, self._version, endpoint)

    def _send(self, endpoint, method = 'GET', **kwargs):
        """
        might want to use json instead of params
        Make the payload dictionary from the kwargs
        """
        url     = self._makebaseurl(endpoint)

        if method == 'GET':
            resp = requests.get(url, auth = self._auth, headers = self._headers, params = kwargs)
        else:
            raise RequestError("Invalid request")

        return resp

    def _get(self, endpoint, **kwargs):
        """
        """
        return self._send(endpoint, 'GET', **kwargs)

class TataAQ(API):
    """
    """
    def __init__(self, version = 'v1.0', **kwargs):
        self._baseurl = 'https://tatacenter-airquality.mit.edu/api'

        super(TataAQ, self).__init__(version = version, baseurl = self._baseurl, **kwargs)

    def ping(self):
        """Ping the server and ensure authentication credentials are up to date.
        """
        return self._get('auth')

    def device(self, sn = None, **kwargs):
        """Required fields: None
        """
        return self._get('device/{}'.format(sn) if sn else 'device', **kwargs)

    @requires_kws(['sn'])
    @makedataframe()
    def data(self, sn, **kwargs):
        """Required Fields: None
        """
        return self._get('device/{}/data/'.format(sn), **kwargs)
