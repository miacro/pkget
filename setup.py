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


def find_files(path, pattern):
    files = glob.glob(os.path.join(path, pattern))
    result = []
    for filename in files:
        if os.path.isdir(filename):
            sub_result = find_files(filename, pattern)
            for i in range(len(sub_result)):
                result.append(sub_result[i])
        else:
            result.append(filename)
    return result


def get_package_data():
    prev_dir = os.getcwd()
    root_dir = os.path.join(os.path.dirname(abspath), "pkget")
    os.chdir(root_dir)
    result = []
    for i in find_files("recipes", "*"):
        result.append(i)
    for i in find_files("config", "*"):
        result.append(i)
    os.chdir(prev_dir)
    return result


def get_data_files():
    return []


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
      package_data= {'pkget': get_package_data()},
      data_files=get_data_files(),
)
