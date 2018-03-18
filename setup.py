# coding: utf-8
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: roman1972@gmail.com
# License: MIT, see LICENSE.txt

from io import open
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import asyncore_wsgi

with open('Readme.rst', 'r', encoding='utf-8') as fo:
    long_descr = fo.read()

setup(
    name='asyncore-wsgi',
    version=asyncore_wsgi.__version__,
    packages=['asyncore_wsgi'],
    url='https://github.com/romanvm/asyncore-wsgi',
    license='MIT',
    author='Roman Miroshnychenko',
    author_email='roman1972@gmail.com',
    description='Asynchronous WSGI and WebSocket server based on asyncore module',
    long_description=long_descr,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server'
    ],
)
