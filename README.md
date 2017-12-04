

'https://local-library-website-jwpbanawan.c9users.io/' and the admin page from 
'https://local-library-website-jwpbanawan.c9users.io/admin'.

## LocalLibrary  Website

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Overview

URL maps to forward the supported URLs (and any information encoded in the URLs) to the appropriate view functions.

View functions to get the requested data from the models, create an HTML page displaying the data, and return it to the user to view in the browser.

Templates used by the views to render the data.



# URLs that we need

The URLs that we're going to need for our pages are:

catalog/ — The home/index page.

catalog/books/ — The list of all books.

catalog/authors/ — The list of all authors.

catalog/book/<id> — The detail view for the specific book with a field primary key of <id> (the default). So for example, /catalog/book/3, for the third book added.

catalog/author/<id> — The detail view for the specific author with a primary key field named <id>. So for example, /catalog/author/11, for the 11th author added.