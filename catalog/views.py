from django.shortcuts import render
from django.views import generic


from models import Book, Author, BookInstance, Genre
# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
     # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'num_visits':num_visits}, # num_visits appended
    )
    
    #added pagination variable here, only applies on class based views
    
    
class BookListView(generic.ListView):
    model = Book
    #thats about it, but u can modify more like these:
    '''Book attributes:
        title = models.CharField(max_length=200)
        author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
        
        summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
        isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
        genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    '''
    #PAGINATION, JUST ADD THIS VARIABLE AND ITS VALUE (check out the updated base_generic.html too!)
    paginate_by = 2
    
    #'context_object_name = 'my_book_list'   # your own name for the list as a template variable
    
    
    #'queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    
    
    ''' !!!! DO THIS IF U WANNA FILTER A CLASS BASED VIEW !!!!'''
    def get_queryset(self):
         return Book.objects.all();
    #    return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # passes object_list to the template, in this case, book_list
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    
    template_name = 'catalog/books_list.html'  # Specify your own template name/location
    
class BookDetailView(generic.DetailView):
    #we dont DIRECTLY use reference models as our main model
    model = Book
    template_name = 'catalog/book_deets.html'
    
    
    
    '''BookInstance model attributes:
         id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
        book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
        imprint = models.CharField(max_length=200)
        due_back = models.DateField(null=True, blank=True)
    
        LOAN_STATUS = (
            ('m', 'Maintenance'),
            ('o', 'On loan'),
            ('a', 'Available'),
            ('r', 'Reserved'),
        )
        
         status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    '''
    
    ''' BY THE WAY THIS IS THE FUNCTION BASED VIEW VERSION OF BOOKDETAILS
    with 404 handling...:
    
        def book_detail_view(request,pk):
            try:
                book_id=Book.objects.get(pk=pk)
            except Book.DoesNotExist:
                raise Http404("Book does not exist")
            
            #this is the code version of it, ONE LINE VERSION FTW!
            
            #book_id=get_object_or_404(Book, pk=pk)
            
            return render(
                request,
                'catalog/book_detail.html',
                context={'book':book_id,}
            )
        
    '''

class AuthorListView(generic.ListView):
    model = Author
    '''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    '''
    
    
    template_name='catalog/authors_list.html'
    
    context_object_name = "authorsList"
    
    
class AuthorDetailView(generic.DetailView):
    model = Author
    

#tip! regular expressions details ehueheuehe
def patterns(request):
    return render(request, 'patterns.html')