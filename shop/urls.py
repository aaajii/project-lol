from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [

    # index/dashboard
    url(r'^$', views.IndexView.as_view(), name='index'),

    # profile
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),

    # vehicle management
    url(r'^vehicle-mgt/$', views.VehicleView.as_view(), name='vehicle'),

    # vehicle -add
    url(r'^vehicle-add/$', views.VehicleAdd.as_view(), name='vehicle-add'),

    # vehicle -upd
    url(r'^vehicle-upd/(?P<pk>\d+)/$', views.VehicleUpd.as_view(), name='vehicle-upd'),

    # vehicle -dlt
    url(r'^vehicle-dlt/(?P<pk>\d+)/delete/$', views.VehicleDlt.as_view(), name='vehicle-dlt'),

    # customer management
    url(r'^customer-mgt/$', views.CustomerView.as_view(), name='customer'),

    # customer -add
    url(r'^customer-add/$', views.CustomerAdd.as_view(), name='cust-add'),

    # customer -update
    url(r'^customer-upd/(?P<pk>\d+)/$', views.CustomerUpd.as_view(), name='cust-upd'),

    # customer -dlt
    url(r'^customer-dlt/(?P<pk>\d+)/delete/$', views.CustomerDlt.as_view(), name='cust-dlt'),

    # technician management
    url(r'^technician-mgt/$', views.TechnicianView.as_view(), name='technician'),

    # technician -add
    url(r'^technician-add/$', views.TechnicianAdd.as_view(), name='tech-add'),

    # technician -upd
    url(r'^technician-upd/(?P<pk>\d+)/$', views.TechnicianUpd.as_view(), name='tech-upd'),

    # technician -dlt
    url(r'^technician-dlt/(?P<pk>\d+)/delete/$', views.TechnicianDlt.as_view(), name='tech-dlt'),

    # Supplier management
    url(r'^supplier-mgt/$', views.SupplierView.as_view(), name='supplier'),

    # supplier -add
    url(r'^supplier-add/$', views.SupplierAdd.as_view(), name='supplier-add'),

    # supplier -upd
    url(r'^supplier-upd/(?P<pk>\d+)/$', views.SupplierUpd.as_view(), name='supplier-upd'),

    # supplier -dlt
    url(r'^supplier-dlt/(?P<pk>\d+)/delete/$', views.SupplierDlt.as_view(), name='supplier-dlt'),

    # Jobs management
    url(r'^jobs-mgt/$', views.JobsView.as_view(), name='jobs'),

    # Jobs -add
    url(r'^jobs-add/$', views.JobsAdd.as_view(), name='jobs-add'),

    # Jobs -upd
    url(r'^jobs-upd/(?P<pk>\d+)/$', views.JobsUpd.as_view(), name='jobs-upd'),

    # Jobs -dlt
    url(r'^jobs-dlt/(?P<pk>\d+)/delete/$', views.JobsDlt.as_view(), name='jobs-dlt'),

    # Parts management
    url(r'^parts-mgt/$', views.PartsView.as_view(), name='parts'),

    # Parts -add
    url(r'^parts-add/$', views.PartsAdd.as_view(), name='parts-add'),

    # Parts -upd
    url(r'^parts-upd/(?P<pk>\d+)/$', views.PartsUpd.as_view(), name='parts-upd'),

    # Parts -dlt
    url(r'^parts-dlt/(?P<pk>\d+)/delete/$', views.PartsDlt.as_view(), name='parts-dlt'),




]
