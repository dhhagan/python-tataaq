import json
import requests
import pandas as pd

from .exceptions import ApiError

__all__ = ['TataAQ']

class API(object):
    """Generic API Base Wrapper
    """
    def __init__(self, **kwargs):
        self._username  = kwargs.pop('username', '')
        self._password  = kwargs.pop('password', '')
        self._version   = kwargs.pop('version', '')
        self._baseurl   = kwargs.pop('baseurl', '')
        self._headers   = {'content-type': 'application/json'}
        self._auth      = (self._username, self._password)

    def _make_url(self, endpoint):
        """Internal method to create a url from an endpoint

            :param endpoint: Endpoint for an API call

            :returns: url
        """
        return "{}/{}/{}".format(self._baseurl, self._version, endpoint)

    def _send(self, uri, method = 'GET', **kwargs):
        """
        """
        uri     = self._make_url(uri)
        params  = kwargs.pop('params', None)

        if method == 'GET':
            try:
                resp = requests.get(
                        uri,
                        auth = self._auth,
                        headers = self._headers,
                        params = params)
            except Exception as e:
                raise ApiError(e)
        else:
            raise ApiError("Invalid method.")

        return resp.status_code, resp.json()

    def _get(self, url, **kwargs):
        """
        """
        return self._send(url, **kwargs)

class TataAQ(API):
    """
    """
    def __init__(self, apikey, version = 'v2.0', **kwargs):
        self._baseurl = 'https://tatacenter-airquality.mit.edu/api'

        super(TataAQ, self).__init__(version = version, baseurl = self._baseurl, username = apikey)

    def ping(self):
        """Check authentication credentials

        >>> status, resp = api.ping()
        {
            'Authentication Check': 'All good!'
        }
        """
        return self._get('auth/')

    def ebam(self, **kwargs):
        """Retrieve E-BAM Data

        >>> params = {'expand': 1, per_page = 2, page = 1}
        >>> status, resp = api.ebam(params = params)
        {
            'data': [
                {
                    'alarm': 0,
                    'ambient_temperature': 27.5,
                    ...
                    },
                    ...
            ],
            'meta': {
                'first_url': 'dummy_url',
                'last_url': 'dummy_url',
                'next_url': 'dummy_url',
                'page': 1,
                'pages': 2667,
                'per_page': 250,
                'prev_page': null,
                'total': 5333
            }
        }
        """
        return self._get('ebam-data', **kwargs)
