'''
Includes helper functions
'''
import pandas as pd

def to_dataframe(response):
    """Turn the API response into a Pandas DataFrame
    """
    return pd.io.json.json_normalize(response)
