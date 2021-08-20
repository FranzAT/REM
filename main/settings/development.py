# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['franzat.eu.pythonanywhere.com']
ALLOWED_HOSTS = get_env_variable('SITE_HOST')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'FranzAT$default',
        'NAME': get_env_variable('DATABASE_NAME'),
#        'USER': 'FranzAT',
        'USER': get_env_variable('DATABASE_USER'),
#        'PASSWORD': 'password set in seperate file',
        'OPTIONS': {'read_default_file': '~/.my.cnf',},
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
#        'HOST': 'FranzAT.mysql.eu.pythonanywhere-services.com',
        'HOST': get_env_variable('DATABASE_HOST'),
    }
}
