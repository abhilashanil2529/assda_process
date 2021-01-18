from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Agency)
admin.site.register(AgencyType)
admin.site.register(AgencyCollection)
admin.site.register(StatusChange)
admin.site.register(AgencyListReference)

