#!/usr/bin/env python

import os
import sys
import setuptools

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='pysensorpush',
      version='0.0.1',
      packages=[ 'pysensorpush' ],
      description='Python interface for the SensorPush API',
      long_description=long_description,
      url='https://github.com/rsnodgrass/pysensorpush',
      author='Ryan Snodgrass',
      author_email='rsnodgrass@gmail.com',
      license='Apache 2.0',
      install_requires=[ 'requests>=2.0' ],
      keywords=[ 'sensorpush', 'home automation', 'humidity', 'temperature' ], 
      zip_safe=True,
      classifiers=[ "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: Apache License",
                    "Operating System :: OS Independent",
      ],
)
