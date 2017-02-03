"""Docstring."""
from functools import wraps
from .exceptions import KeywordError
import pandas as pd
from .utils import to_naive_timestamp


def requires_kws(required_kwargs):
    """Require certain kw args."""
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            for kw in required_kwargs:
                if kw not in kwargs.keys():
                    raise KeywordError("{} is a required kw arg".format(kw))
            return f(*args, **kwargs)
        return wrapped_f
    return wrap


def makedataframe():
    """Turn the resp into a DataFrame."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            dataframe = kwargs.get('dataframe', False)

            if dataframe:
                resp = f(*args, **kwargs)

                if resp.status_code == 200:
                    data = resp.json()['data']
                    meta = resp.json()['meta']

                    if len(data) > 0:
                        df = pd.io.json.json_normalize(data)

                        # Check for datetime columns
                        if 'timestamp' in df.columns:
                            df['timestamp'] = pd.to_datetime(df['timestamp'])

                        if 'timestamp_local' in df.columns:
                            df['timestamp_local'] = pd.to_datetime(
                                                        df['timestamp_local'].apply(lambda x: to_naive_timestamp(x)))
                    else:
                        df = pd.DataFrame()

                return meta, df

            return f(*args, **kwargs)
        return decorated_function
    return decorator
