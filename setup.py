# -*- encoding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages

assert sys.version_info >= (2, 7), "Python 2.7+ required."

current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, 'README.rst')) as readme_file:
    with open(os.path.join(current_dir, 'CHANGES.rst')) as changes_file:
        long_description = readme_file.read() + '\n' + changes_file.read()

sys.path.insert(0, current_dir + os.sep + 'src')
VERSION = ('0', '1', '0-alpha')
release = ".".join(str(num) for num in VERSION)

setup(
    name='inkpy',
    version=release,  # release,
    author='Kamil Warguła',
    author_email='kwargula@gmail.com',
    description="InkPy - provide tool to fill Django style template in odt file",
    long_description=long_description,
    url='https://github.com/quamilek/InkPy',
    keywords='',
    platforms=['any'],
    license='Apache Software License v2.0',
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    zip_safe=False,  # because templates are loaded from file path
    install_requires=[
        'django>=1.4.13',
        'django_rq==0.4.5',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        'Natural Language :: English',
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
