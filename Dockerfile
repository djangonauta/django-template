FROM nikolaik/python-nodejs:python3.12-nodejs22

WORKDIR /usr/app

RUN mkdir -p /run/gunicorn/
RUN mkdir -p /var/log/gunicorn
RUN mkdir -p /etc/nginx/ssl

RUN npm install -g yuglify
RUN apt update
RUN apt install build-essential libbz2-dev libffi-dev libfreetype6-dev \
    libjpeg-dev liblcms2-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libssl-dev \
    libtiff5-dev libwebp-dev libxml2-dev make zlib1g-dev \
    libgdal-dev graphviz libgraphviz-dev libldap2-dev libsasl2-dev nginx -y

RUN pip3 install -U pip wheel setuptools poetry

COPY . .
COPY ./docker.cfg/nginx.conf /etc/nginx/nginx.conf
COPY ./docker.cfg/cert.pem /etc/nginx/ssl/
COPY ./docker.cfg/key.pem /etc/nginx/ssl/
COPY ./docker.cfg/pass /etc/nginx/ssl/

RUN chmod 400 -R /etc/nginx/ssl/