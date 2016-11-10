# Django Basics

Django project consists of **applications** and **configurations**.  
Django app is a specific part of a website that is associated with some functionality.  
A website can contain Blog App, Auth App, Poll App, etc.  
The idea is that you can use a given app and transfer it to another project with minimal difficulties.

## Project setup 

Starting a project: `django-admin startproject { project_name }`  
Creating an app: `python manage.py startapp { app_name }`  

### Core Structure

- `__init__.py` , a blank Python script whose presence indicates to the Python interpreter that the directory is a Python package;
- `settings.py` , the place to store all of your Django project’s settings;
- `urls.py` , a Python script to store URL patterns for your project; and
- `wsgi.py` , a Python script used to help run your development server and deploy your project to a production environment.

### Application structure

- `__init__.py` , a blank Python script whose presence indicates to the Python interpreter that the directory is a Python package;
- `admin.py` , where you can register your models so that you can benefit from some Django machinery which creates an admin interface for you;
- `apps.py` , that provides a place for any application specific configuration;
- `models.py` , a place to store your application’s data models - where you specify the entities and relationships between data;
- `tests.py` , where you can store a series of functions to test your application’s code;
- `views.py` , where you can store a series of functions that handle requests and return responses;
- `migrations` directory, which stores database specific information related to your models.

### Starting development

After creating an app, we need to add this newly created app to the `INSTALLED_APPS` in `settings.py` file.  
When working with django, most of the development is done in `models` and `views`.
