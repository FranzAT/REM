# REM
Real Estate Management

Based on:
- Python
- Django Framework
- MySQL database
- Bootstrap 4 Framework
- jQuery JavaScript library

Running on:
- http://eu.pythonanywhere.com
- virtual environments for development / testing / staging / production

Goodies:
- social media login with django-allauth
- i18n internationalization and localisation

## Installation
1. Create virutal environments for development and testing `$mkdir --python=/home/<username>/.local/bin/python3 dev`
2. Install dependencies for each of the environments `$ pip install -r requirements/development.txt`
3. Create project root folder `$ mkdir REM`
4. Clone GitHub repository
5. SECRET_KEY is in ~/REM/.env (and excluded with .gitignore for version control).
6. virtual environment specific settings are maintained outside version control in ~/.virtualenvs/dev/bin/postactivate
```
#!/bin/bash
# This hook is sourced after this virtualenv is activated.
export DJANGO_SETTINGS_MODULE="main.settings.development"
# SECURITY WARNING: keep the secret key used in production secret!
set -a; source ~/REM/.env; set +a
```
7. virtual environment specific settings are closed by ~/.virtualenvs/dev/bin/predeactivate
```
#!/bin/bash
# This hook is sourced before this virtualenv is deactivated.
unset DJANGO_SETTINGS_MODULE
unset SECRET_KEY
```
8. adapt MySQL credentials accordingly to environment in ~/REM/main/settings/development.py

## Usage
[https://franzat.eu.pythonanywhere.com](https://franzat.eu.pythonanywhere.com/)

## Documentation
[https://real-estate-management.readthedocs.io](https://real-estate-management.readthedocs.io/)
