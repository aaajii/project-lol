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

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
        url(r'^accounts/', include('django.contrib.auth.urls')),
    ]
    
    
'''This automatically adds:
    ^accounts/login/$ [name='login']
    ^accounts/logout/$ [name='logout']
    ^accounts/password_change/$ [name='password_change']
    ^accounts/password_change/done/$ [name='password_change_done']
    ^accounts/password_reset/$ [name='password_reset']
    ^accounts/password_reset/done/$ [name='password_reset_done']
    ^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
    ^accounts/reset/done/$ [name='password_reset_complete']
'''