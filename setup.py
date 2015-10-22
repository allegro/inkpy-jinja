# -*- encoding: utf-8 -*-
from setuptools import setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

setup(
    name='inkpy_jinja',
    version='0.1.0',
    author='Grupa Allegro Sp. z o.o. and Contributors',
    author_email='pylabs@allegro.pl',
    description='inkpy-jinja - it\'s fork of powerful library called InkPy',
    long_description=readme + history,
    url='https://github.com/allegro/inkpy-jinja',
    keywords='',
    platforms=['any'],
    license='Apache Software License v2.0',
    packages=['inkpy_jinja'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jinja2',
        'unotools==0.3.3',
    ],
    extras_require={
        'service': ['rq'],
    },
    tests_require=[
        'flake8',
    ],
    test_suite='tests.main',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
