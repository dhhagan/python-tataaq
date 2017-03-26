# py-tata
Python wrapper for the Tata Center Air Quality website

# Installation

Clone or download the zip file and run the following:

    python3 setup.py install (--upgrade)

# Authentication Credentials

You must obtain an API Key from the portal using your current TataAQ account.

# Basic Use

    import tataaq

    api = tataaq.TataAQ(apikey='key_goes_here')

    status, resp = api.ping()

## Get E-BAM Data

    params = {
        'expand': True,
        'per_page': 250,
        'page': 1
    }

    status, resp = api.ebam(params=params)

    # Access Meta Information
    resp['meta']

    # Access Data
    resp['data']
