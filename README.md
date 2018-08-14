

`python-tataaq` is an object-first python wrapper for the [Tata Center Air Quality API][1].

By David H Hagan, MIT

# Introduction

This library provides a pure python interface to the Tata Center Air Quality Project API.
It works with Python versions 2.7+ and Python3.

## Installation

There are a couple of easy options for installation of the package:

For development purposes, clone the repo locally:

    $ git clone git@github.com/dhhagan/py-tata.git
    $ cd py-tata
    $ python3 setup.py install

Or, install the library directly from GitHub (preferred) using pip:

    $ pip install git+https://github.com:dhhagan/py-tata.git


## Authentication/API Key

To use the API, you must have an API key (http basic auth), which can be found by logging on to your account and adding a key. You should then save your key as an
environment variable (the process is unique to your operating system). For example, on a
Mac with High Sierra, you can save the variable to your bash profile:

  1. Open the file:

      `$ nano ~/.bash_profile`

  2. Add a line to the file with:

        `export TATAAQ_APIKEY=<api-key-goes-here>`
  3. Open a new terminal or source the file:

        `$ source ~/.bash_profile`


## Docs

Please see the [docs folder][2] for documentation.

## Unittests

Tests can be run using the following command (with and without coverage)

    $ python3 setup.py test

Or, with coverage:

    $ coverage run --source py-tata setup.py test
    $ coverage report -m

[1]: https://tatacenter-airquality.mit.edu/docs
[2]: /docs
