#!/usr/bin/env python

from setuptools import setup

# TODO: automate all the following
# TODO: rhc app create bla blab
# TODO: git add upstream
# TODO: rm requirements.txt wsgi.py
# TODO: django-admin startproject
# TODO: deply collectstatic requires STATIC_ROOT in settings: STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# TODO: rhc env set vars

setup(

    # GETTING-STARTED: set your app name:
    name='YourAppName',

    # GETTING-STARTED: set your app version:
    version='1.0',

    # GETTING-STARTED: set your app description:
    description='OpenShift App',

    # GETTING-STARTED: set author name (your name):
    author='Your Name',

    # GETTING-STARTED: set author email (your email):
    author_email='example@example.com',

    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',

)
