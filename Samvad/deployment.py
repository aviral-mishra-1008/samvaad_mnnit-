import os
from .settings import *
from .settings import BASE_DIR


SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ["https://"+ os.environ['WEBSITE_HOSTNAME']]
DEBUG = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
l = connection_string.split(' ')
parameters = dict()

for i in l:
    stringNeeded = i.split('=')
    parameters[stringNeeded[0]] = stringNeeded[1]


DATABASES = {  
    'default':{
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : parameters['dbname'],
        'HOST' : parameters['host'],
        'USER' : parameters['user'],
        'PASSWORD' : parameters['password'],
        'OPTIONS':{"sslmode":"require"},
    }
}
