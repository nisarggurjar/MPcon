# Fashion Hub

## To Start New Project 

django-admin startproject <project name>

## To Runserver 

python manage.py runserver

## To make migrations

python manage.py makemigrations

## To migrate changes 

python manage.py migrate

## To Start a App

python manage.py startapp <app name>

##### Always add app name in installed_app list present in settings file 

## To create super user

python manage.py createsuperuser


# Template Tags

1. To load static
{%  load static %}

2. To add Static Files 
{% static '<file path>' %}

3. To add URL routing 
{% url '<url_name>' %}

4. To extend a html file
{% extends '<file_name>' %}

5. To Make a Block
{% block <block_body> %} {% endblock <block_body> %}

6. if
{% if <condition> %}
.....
....
{% endif %}

7. if else
{% if <condition> %}
...
...
...
{% else %}
...
...
...
{% endif %}

8. if elif
{% if <condition> %}
...
...
...
{% elif <condition> %}
...
...
...
{% elif <condition> %}
...
...
...
{% elif <condition> %}
...
...
...
{% endif %}

9. For 
{% for o in some_list %}
    ...
    ...
    ...
{% endfor %}