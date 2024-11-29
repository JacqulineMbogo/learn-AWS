### Install python

    > Download desired version from https://www.python.org/downloads/
### Django Project Setup
CD into a new folder and name it as you wish
#### Create virtual environment
    > pythin3 -m venv venv
#### Activate Virtual Environment
    > source venv/bin/activate
#### Install django
    > pip install django
#### Create django project
    > django-admin startproject projectname

### Django App Setup
    > django-admin startapp appname
Remember to add your app in INSTALLED_APPS in your settings.py

### RunServer
    > python manage.py runserver

### RunMigrations
    > python manage.py makemigrations
    > python manage.py migrate

### Create superuser
    > python manage.py createsuperuser
     U: admin
     P: test
