FROM ubuntu:latest
MAINTAINER sri
RUN apt update
RUN apt install apache2 wget unzip -y
ADD  sh.tar.gz /var/www/html
CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["/usr/sbin/apache2ctl"]
EXPOSE 80
WORKDIR /var/www/html

