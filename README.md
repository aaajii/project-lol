

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


the main things that Django's form handling does are:

Display the default form the first time it is requested by the user.

1.) The form may contain blank fields (e.g. if you're creating a new record), or it may be pre-populated with initial values (e.g. if you are changing a record, or have useful default initial values).

2.) The form is referred to as unbound at this point, because it isn't associated with any user-entered data (though it may have initial values).

3.) Receive data from a submit request and bind it to the form.

4.) Binding data to the form means that the user-entered data and any errors are available when we need to redisplay the form.

5.) Clean and validate the data.

6.) Cleaning the data performs sanitisation of the input (e.g. removing invalid characters that might potentially used to send malicious content to the server) and converts them into consistent Python types.

7.) Validation checks that the values are appropriate for the field (e.g. are in the right date range, aren't too short or too long, etc.)

8.) If any data is invalid, re-display the form, this time with any user populated values and error messages for the problem fields.

9.) If all data is valid, perform required actions (e.g. save the data, send and email, return the result of a search, upload a file etc.)

10.) Once all actions are complete, redirect the user to another page.
