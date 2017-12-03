

'https://local-library-website-jwpbanawan.c9users.io/' and the admin page from 
'https://local-library-website-jwpbanawan.c9users.io/admin'.

## LocalLibrary  Website

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Overview

The Django admin application can use your models to automatically build a site area that you can use to create, view, update, and delete records.
This can save you a lot of time during development, making it very easy to test your models and get a feel for whether you have the right data.
The admin application can also be useful for managing data in production, depending on the type of website.
The Django project recommends it only for internal data management (i.e. just for use by admins, or people internal to your organization),
as the model-centric approach is not necessarily the best possible interface for all users, and exposes a lot of unnecessary detail about the models. 