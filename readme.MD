# Fashion Hub

## To Start New Project 

django-admin startproject &lt;project name&gt;

## To Runserver 

python manage.py runserver

## To make migrations

python manage.py makemigrations

## To migrate changes 

python manage.py migrate

## To Start a App

python manage.py startapp &lt;app name&gt;

##### Always add app name in installed_app list present in settings file 

## To create super user

python manage.py createsuperuser


# Template Tags

1. To load static
{%  load static %}

2. To add Static Files 
{% static '&lt;file path&gt;' %}

3. To add URL routing 
{% url '&lt;url_name&gt;' %}

4. To extend a html file
{% extends '&lt;file_name&gt;' %}

5. To Make a Block
{% block &lt;block_body&gt; %} {% endblock &lt;block_body&gt; %}

6. if
{% if &lt;condition&gt; %}
.....
....
{% endif %}

7. if else
{% if &lt;condition&gt; %}
...
...
...
{% else %}
...
...
...
{% endif %}

8. if elif
{% if &lt;condition&gt; %}
...
...
...
{% elif &lt;condition&gt; %}
...
...
...
{% elif &lt;condition&gt; %}
...
...
...
{% elif &lt;condition&gt; %}
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