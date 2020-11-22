#!/usr/bin/env python


from setuptools import setup


setup(
    name='dota2_api',
    version='1.0.0',
    description='Finds the DOTA 2 teams with the most combined player experience.',
    url='https://docs.opendota.com/',
    author='Brent Fosdick',
    author_email='brent@fosdick.io',
    packages=[
        'dota2_api',
    ],
    install_requires=[
        'argparse',
        'pyyaml',
        'requests'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
