# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['franzat.eu.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'FranzAT$default',
        'USER': 'FranzAT',
#        'PASSWORD': 'password set in seperate file',
        'OPTIONS': {'read_default_file': '~/.my.cnf',},
        'HOST': 'FranzAT.mysql.eu.pythonanywhere-services.com',
    }
}
