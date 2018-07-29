"""A library that provides a Python interface to the Tata Center Air Quality API"""

import requests
import logging
import warnings
import os

from tataaq import (
    __version__,
)

from tataaq.utils import to_naive_timestamp
from tataaq.exceptions import TataRequestError, RequestKeywordError

logger = logging.getLogger(__name__)

class Api(object):
    """
    """
    def __init__(self,
                    apikey=None,
                    base_url=None,
                    input_encoding=None,
                    request_headers=None,
                    debugHTTP=False,
                    sleep_on_rate_limit=False):
        """Initialize a new tataaq.Api object.

        Args:
            apikey (str):
                Your api key. If None, it will be sourced from your environ vars
            ...
        """
        pass

        if os.environ:
            pass

        self._debugHTTP = debugHTTP

        if debugHTTP:
            logger.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
