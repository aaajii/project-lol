

'https://local-library-website-jwpbanawan.c9users.io/' and the admin page from 
'https://local-library-website-jwpbanawan.c9users.io/admin'.

## LocalLibrary  Website

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Overview

In this tutorial we're going to complete the first version of the LocalLibrary website by adding list 
and detail pages for books and authors (or to be more precise, we'll show you how to implement the book pages,
and get you to create the author pages yourself!)