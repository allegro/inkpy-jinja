FROM ubuntu:14.04
MAINTAINER PyLabs pylabs@allegrogroup.com

# set UTF-8 locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 python3-dev python3-pip python3-uno \
    libreoffice-writer openjdk-7-jre unoconv \
    libreoffice-script-provider-python uno-libs3 \
    supervisor

ENV PROJECT_SRC=.
ENV PROJECT_HOME=/srv
ENV PROJECT_PATH=/srv/inkpy-jinja

COPY $PROJECT_SRC $PROJECT_PATH

WORKDIR $PROJECT_PATH

RUN pip3 install -e .
RUN pip3 install -e .[service]

RUN cp contrib/supervisor.conf /etc/supervisor/conf.d/pdf_worker.conf

CMD supervisord -n
