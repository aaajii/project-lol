# Use include() to add URLS from the catalog application 
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^catalog/', include('catalog.urls')),
    url(r'^admin/', admin.site.urls),
]

#Add URL maps to redirect the base URL to our application

from django.views.generic import RedirectView
urlpatterns += [
    #r'^$' is the localhost:8080, or the home page.
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
]
