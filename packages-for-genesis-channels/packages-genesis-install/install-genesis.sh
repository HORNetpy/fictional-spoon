#!/bin/bash

# install django
sudo dpkg -i django-package.deb

# install PostgreSQL and Zabbix
sudo apt-get install postgresql zabbix-server-pgsql zabbix-frontend-php zabbix-agent python-psycopg2 libapache2-mod-wsgi libapache2-mod-auth-pam libapache2-mod-proxy-html python-six

# install Genesis
sudo dpkg -i genesis.deb

#
sudo service postgresql restart