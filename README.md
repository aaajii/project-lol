

'https://local-library-website-jwpbanawan.c9users.io/' and the admin page from 
'https://local-library-website-jwpbanawan.c9users.io/admin'.

## LocalLibrary  Website

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Overview for this branch

We'll do a few of the ways you can create and work with forms, and in particular, how the generic editing form views can significantly reduce the amount of work you need to do to create forms to manipulate your models. Along the way we'll extend our LocalLibrary application by adding a form to allow librarians to renew library books, and we'll create pages to create, edit and delete books and authors (reproducing a basic version of the form shown above for editing books).

lets git gud!