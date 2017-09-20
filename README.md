# py-tata
Python wrapper for the Tata Center Air Quality website

# Installation

There are several options for installation of the package and are outlined here:

## Clone and Install

    $ git clone git@github.com/dhhagan/py-tata.git
    $ cd py-tata
    $ python3 setup.py install

## Download zip file and install from source

Download the zip file, navigate to the directory you saved it in, and run the following:

    $ python3 setup.py install (--upgrade)

## Install directly from GitHub (preferred)

    $ pip install git+https://github.com:dhhagan/py-tata.git

# Authentication Credentials

You must obtain an API Key from the portal using your current TataAQ account.

# Basic Use

    import tataaq

    api = tataaq.TataAQ(apikey='key_goes_here')

    status, resp = api.ping()

## Docs

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

## Unittests

Tests can be run using the following command (with and without coverage)

    $ python3 setup.py test

With coverage:

    $ coverage run --source py-tata setup.py test
    $ coverage report -m
