from django.contrib import admin
from .models import *

admin.site.register(JobType)
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Technician)
admin.site.register(Supplier)
admin.site.register(Job)
admin.site.register(JobOrders)
admin.site.register(JobOrderDetail)
admin.site.register(JobPartUsage)
admin.site.register(PartsOrder)
admin.site.register(PartsOrderDetail)
admin.site.register(PartsReceived)
admin.site.register(PartsRecievedDetail)
admin.site.register(Parts)
admin.site.register(Collections)
admin.site.register(CollectionDetail)
admin.site.register(Payments)
admin.site.register(PaymentsDetail)

