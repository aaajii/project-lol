from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$',views.index, name='index'),
        url(r'^books/$', views.BookListView.as_view(), name='books'),
        url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
        url(r'^authors$',views.AuthorListView.as_view(), name="authors"),
        url(r'^author/(?P<pk>\d+)$',views.AuthorDetailView.as_view(), name="author-detail")
    ]
   
#for the borrowing functionality
urlpatterns += [   
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

#for librarians book list
urlpatterns += [   
    url(r'^borrowed/$', views.LoanedBooksLibrarianListView.as_view(), name='all-borrowed'),
]