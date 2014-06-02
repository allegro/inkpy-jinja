=====
InkPy
=====


.. image:: https://badge.fury.io/py/inkpy.svg
    :target: http://badge.fury.io/py/inkpy

.. image:: https://travis-ci.org/quamilek/InkPy.svg?branch=develop
    :target: https://travis-ci.org/quamilek/InkPy
    
.. image:: https://coveralls.io/repos/quamilek/InkPy/badge.png
  :target: https://coveralls.io/r/quamilek/InkPy




Django app provide interface to fill Django style template in odt file, and
additionally convert odt to pdf file. Can be run synchronously or asynchronously mode.



Configurations
~~~~~~~~~~~~~~

This tool provide interface to fill Django style template in odt file.
Your task is to provide a python script which takes 2 arguments:
odt file path, and the path to save the file pdf.

The recommended way is to use the services LibreOffice / OpenOffice.org,
which provides conversion from odt file to pdf from the console or Python script.

We recommend to use the library PyODConverter:  https://github.com/dieselpoweredkitten/pyodconverter

We need also to define the value in the configuration file, and add the application to INSTALLED_APPS::

    INKPY = {
        'script_path': '/path/to/your/convert/script.py',
        'tmp_dir': '/tmp/inkpy'
    }
    INSTALLED_APPS = INSTALLED_APPS + ['inkpy',]


To install LibreOffice in Ubuntu use::

  $ sudo apt-get install libreoffice libreoffice-common openjdk-7-jre unoconv

To run LibreOffice service use::

  $ soffice --nologo --headless --nofirststartwizard --accept='socket,host=127.0.0.1,port=2002,tcpNoDelay=1;urp;StarOffice.Service'
