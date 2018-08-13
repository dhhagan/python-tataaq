# -*- coding: utf-8 -*-

import os
import json
import logging
import requests

from . import __name__, __version__
from . utils import list_to_dataframe

try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse

GET = 'GET'
PUT = 'PUT'
DELETE = 'DELETE'
POST = 'POST'

class TokenError(Exception):
    pass

class NotFoundError(Exception):
    pass

class NotPermittedError(Exception):
    pass

class JSONReadError(Exception):
    pass

class DataReadError(Exception):
    pass

class BadRequestError(Exception):
    pass


class BaseAPI(object):
    """Basic API class."""
    def __init__(self, token=None, *args, **kwargs):
        if token:
            self.token = token
        else:
            self.token = os.environ.get("TATAAQ_APIKEY", None)

        self.endpoint = "https://tatacenter-airquality.mit.edu/api/v1.0/"

        self._log = logging.getLogger(__name__)

        # set kwargs
        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])

    def _make_request(self, endpoint, type=GET, params=None):
        """Perform an API request.

        Examples
        --------

        >>> resp = api._make_request(endpoint='device/', params=dict(per_page=2))
        """
        if params is None:
            params = dict()

        if not self.token:
            raise TokenError("No API token provided. Please provide an API token.")

        # join the url
        url = urlparse.urljoin(self.endpoint, endpoint)

        headers = {'Content-Type': 'application/json'}
        identity = lambda x: x
        json_dumps = lambda x: json.dumps(x)

        lookup = {
            GET: (requests.get, {}, 'params', identity),
            POST: (requests.post, headers, 'data', json_dumps),
            PUT: (requests.put, headers, 'data', json_dumps),
            DELETE: (requests.delete, headers, 'data', json_dumps)
        }

        requests_method, headers, payload, transform = lookup[type]

        # create logging string
        agent = "{0}/{1} {2}/{3}".format('python-tataaq',
                                         __version__,
                                         requests.__name__,
                                         requests.__version__)

        # set the kwargs
        kwargs = {'headers': headers, payload: transform(params)}

        # set the authentication params
        auth = (self.token, None)

        # log the debug string
        self._log.debug("{} {} {}: {} {}".format(type, url, payload, params, agent))

        return requests_method(url, auth=auth, **kwargs)

    def _deal_with_pagination(self, endpoint, method, params, data):
        """Perform multiple calls to retrieve all data when the results are paginated.

        If results aren't paginated, return the raw data
        """
        # start by flattening the first request we already made - this will be an array
        all_data = data.get('data')

        # iterate and make more request
        while data.get("meta", {}).get("next_url"):
            url, query = data.get('meta').get('next_url').split("?", 1)

            # remove in production
            url = url.replace("https", "http")

            for key, value in urlparse.parse_qs(query).items():
                params[key] = value

            # reissue the request for the next page
            data = self._make_request(url, method, params).json()

            # append the data to all_data
            [all_data.append(item) for item in data.get('data')]

        return all_data

    def fetch_data(self, endpoint, type=GET, params=None):
        """Make a get call - this method will safely handle pagination
        if needed.
        """
        if params is None:
            params = dict()

        if type == 'GET': # set a sane per_page default in case paginated requests are made
            params.setdefault("per_page", 200)

        req = self._make_request(endpoint, type, params)

        # check for errors
        if req.status_code == 404:
            raise NotFoundError()

        if req.status_code == 403:
            raise NotPermittedError()

        if req.status_code == 400:
            raise BadRequestError()

        try:
            data = req.json()
        except ValueError as e:
            raise JSONReadError("Could not decode json data.")

        if not req.ok:
            raise DataReadError("Could not read data from tatacenter-airquality.com")

        # deal with pagination if needed
        pages = data.get("meta", None)
        if pages is not None:
            if pages.get("next_url") and pages.get("page") != pages.get("pages"):
                data = self._deal_with_pagination(endpoint, type, params, data)
            else:
                data = data.get('data')
        else:
            pass

        return data

    def __str__(self):
        return "<%s>" % self.__class__.__name__

    def __unicode(self):
        return u"<%s>" % self.__str__

    def __repr__(self):
        return str(self)
