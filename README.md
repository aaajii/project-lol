

'https://local-library-website-jwpbanawan.c9users.io/' and the admin page from 
'https://local-library-website-jwpbanawan.c9users.io/admin'.

## LocalLibrary  Website

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Notes

Tutorial in creating this website: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website

## Steps in adding applications:
1.) Register app in settings.py under 'INSTALLED_APPS'

2.) Hookup the url mapper



## If you do clone this workspace and want to develop on your own, please do:

1.) migrate the workspace

2.) Config the settings.py 

    Check if:
        Database is set correctly
        
        Timezone is set correctly
        
        Debug is set to true (for development)
        
        
        
Thats about it. ehe