# CRM Project Basic

### Setup simple server

 1. Install python
 2. [Upgrade pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip) by using command `python -m pip install -U pip`
 3. [Install django](https://docs.djangoproject.com/en/3.1/topics/install/#installing-an-official-release-with-pip) `py -m pip install Django` or `pip install Django`
 4. [Create new project](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-a-project) `django-admin startproject crm` & `cd crm`
 5. [Run the server](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#the-development-server) `python manage.py runserver`
 6. Show in browser __http://127.0.0.1:8000__
 
 
### [Django Admin](https://docs.djangoproject.com/en/3.1/ref/django-admin/#)


### Making app 

 7. [Creating an app](https://docs.djangoproject.com/en/3.1/ref/django-admin/#startapp) `python manage.py startapp accounts`
 
### Making templates

 8. Make a folder with name of **templates** inside an app
 9. [Overriding templates](https://docs.djangoproject.com/en/3.1/howto/overriding-templates/) [templating tutorial ](https://docs.djangoproject.com/en/3.1/intro/tutorial03/)
 10. [Extending an overridden template](https://docs.djangoproject.com/en/3.1/howto/overriding-templates/#extending-an-overridden-template)
 11. [Built in tags and filter](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/)

### [Managing static files](https://docs.djangoproject.com/en/3.1/howto/static-files/)
 
 12. Make sure that django.contrib.staticfiles is included in your INSTALLED_APPS.
 13. In your settings file, define STATIC_URL, for example: `STATIC_URL = '/static/'`
 
 
### Database Models 
 14. [Migrating database](https://docs.djangoproject.com/en/3.1/ref/django-admin/#migrate) `python manage.py migrate`
 15. [For SqLite](https://docs.djangoproject.com/en/3.1/topics/migrations/) 
 ```
python manage.py makemigrations
python manage.py migrate
 ```

### [Create admin user](https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user) 

16. `python manage.py createsuperuser`


 
 