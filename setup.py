'''
	Python wrapper for the TataAQ API
	Written originally by David H Hagan
	July 2016

	Updated August 2018
'''
import os

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name='python-tataaq',
	version="0.3.0",
	description='Python wrapper for the TataAQ API',
	keywords=['TataAQ', 'MIT', 'Air Quality', 'Tata Center'],
	author='David H Hagan',
	author_email='dhagan@mit.edu',
	url='https://github.com/dhhagan/py-tata',
	license='MIT',
	packages=['tataaq'],
	test_suite='tests',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Operating System :: OS Independent',
		'Intended Audience :: Science/Research',
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Scientific/Engineering :: Atmospheric Science',
		'Topic :: Software Development',
		'Topic :: Software Development :: Libraries :: Python Modules'
	]
)
