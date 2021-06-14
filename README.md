# django-database-prefix
Ables you to set Django's database tables prefix, as a result you can run multiple Django projects using single database, without any actions on the unmanaged tables.

## Installation
Install using pip
```
pip install django-database-prefix
```
Add `django-database-prefix` at the top of the `INSTALLED_APPS` to make it initialized first.
```
'django_database_prefix',
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
```

## Configuration
Set string value for `DB_PREFIX` in the settings.py
```
DB_PREFIX = 'app1_'
```
In result you'll have `app1_django_session` talbe names pattern.