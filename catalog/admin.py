from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)



# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    
# Controlling which fields are displayed and laid out
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator @admin.register
# (this does exactly the same thing as the admin.site.register() syntax):
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

'''Once you've got a lot of items in a list, it can be useful to be able to filter which items are displayed.
This is done by listing fields in the list_filter attribute. '''


''' Currently all of our admin classes are empty (see "pass") so the admin behaviour 
will be unchanged! We can now extend these to define our model-specific admin behaviour'''

