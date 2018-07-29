Python TataAQ

A Python wrapper around the Tata AQ API.

By David H Hagan, MIT

# Introduction

This library provides a pure python interface to the Tata Center Air Quality Project API.
It works with Python versions 2.7+ and Python3.

## Installing

There are several options for installation of the package; you can install the library by
first cloning the GitHub repo and installing from source:

    $ git clone git@github.com/dhhagan/py-tata.git
    $ cd py-tata
    $ python3 setup.py install

You can also download the zip file and install from source:

  1. download the zip file
  2. `$ python3 setup.py install (--upgrade)`

Or, you could install the library directly from GitHub (preferred):

    $ pip install git+https://github.com:dhhagan/py-tata.git


## Authentication Credentials

To use the API, you must have an API key (http basic auth), which can be found by
logging on to your account and adding a key. You should then save your key as an
environment variable (the process is unique to your operating system). For example, on a
Mac with High Sierra, you can open your bash profile and save the variable as follows:

  1. nano ~/.bash_profile
  2. add a line to the file with:

        `export TATAAQ_APIKEY=<api-key-goes-here>`


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
