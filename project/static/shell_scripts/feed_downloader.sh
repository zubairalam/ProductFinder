#!/bin/bash

# activate 'project' virtualenv
. /home/vagrant/.virtualenvs/project/bin/activate

# change directory to /vagrant/project
cd /vagrant/project

# run django management command
/home/vagrant/.virtualenvs/project/bin/python manage.py feed_downloader

# get back to initial directory
cd -
