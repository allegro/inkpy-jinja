===========
inkpy_jinja
===========

.. image:: https://badge.imagelayers.io/allegr/inkpy_jinja:latest.svg
    :target: https://imagelayers.io/?images=allegro/inkpy_jinja:latest


Module provide interface to fill template in odt file and convert odt to pdf file via LibreOffice.


Configurations
~~~~~~~~~~~~~~

To install LibreOffice in Ubuntu use::

  $ sudo apt-get install libreoffice-writer openjdk-7-jre unoconv
  $ sudo apt-get install libreoffice-script-provider-python uno-libs3


.. note:: ``LibreOfficePDFBackend`` works only with Python 3.x and LibreOffice version 4.x.

To run LibreOffice as a service use::

  $ soffice --nologo --headless --nofirststartwizard --accept='socket,host=127.0.0.1,port=2002,tcpNoDelay=1;urp;StarOffice.Service'

If you want use ``inkpy-jinja`` like service you must install ``rq`` and run following command::

  $ RQ_REDIS_URL=redis://host:port rqworker queue_name


where::

  * ``host:port`` - connection pair to redis server,
  * ``queue_name`` - name of queue.


Docker installation (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pull docker image::

  $ docker pull inkpy allegro/inkpy

and run it::

  $ docker run --net host allegro/inkpy:latest
