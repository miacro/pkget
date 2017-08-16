#!/usr/bin/env python
from setuptools import setup, find_packages
import os
import glob
abspath = os.path.abspath(__file__)
version = None
with open('pkget/version.py') as version_file:
    exec(version_file.read())

requirements = [
    'PyYaml',
]


def get_scripts():
    prev_dir = os.getcwd()
    root_dir = os.path.dirname(abspath)
    os.chdir(root_dir)
    result = glob.glob("bin/pkget")
    os.chdir(prev_dir)
    return result

long_description = ''
setup(name='pkget',
      version=version,
      description='package installer',
      long_description=long_description,
      url='',
      author='miacro',
      author_email='fqguozhou@gmail.com',
      maintainer='miacro',
      maintainer_email='fqguozhou@gmail.com',
      packages=find_packages(exclude=['test.*', 'test', 'tests.*', 'tests']),
      install_requires=requirements,
      classifiers=[
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
      ],
      scripts=get_scripts(),
)
