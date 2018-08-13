"""Includes helper functions."""

import pandas as pd

def list_to_dataframe(data, **kwargs):
    """Convert an array of dictionaries to a pandas dataframe
    """
    TIMESTAMP_COL_NAMES = ['timestamp', 'timestamp_iso', 'last_updated']

    if not isinstance(data, list):
        raise TypeError("data must be a list")

    data = pd.io.json.json_normalize(data)

    for col in TIMESTAMP_COL_NAMES:
        if col in data.columns:
            try:
                data[col] = data[col].map(pd.to_datetime, **kwargs)

                # if timestamp or last_updated, force to UTC
                if col in ['timestamp', 'last_updated']:
                    try:
                        data[col] = data[col].apply(lambda x: x.tz_localize("UTC"))
                    except Exception as e:
                        pass
            except Exception as e:
                pass


    return data
