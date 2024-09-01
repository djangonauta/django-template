FROM nginx:1.25

RUN mkdir -p /etc/nginx/ssl
RUN chmod 400 -R /etc/nginx/ssl/
COPY ./cert.pem /etc/nginx/ssl/
COPY ./key.pem /etc/nginx/ssl/
COPY ./pass /etc/nginx/ssl/

COPY ./nginx.conf /etc/nginx/nginx.conf
