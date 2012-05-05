#!/usr/bin/env python

from distutils.core import setup

version = __import__('pychimp').__version__

setup(
    name='pychimp',
    version=version,
    description='A reusable Django app for queuing the sending of email',
    author='Hunter Ford',
    author_email='hunterford@gmail.com',
    url='http://code.google.com/p/pychimp/',
    packages=[
        'pychimp',
    ],
    package_dir={'pychimp': 'pychimp'},
)
