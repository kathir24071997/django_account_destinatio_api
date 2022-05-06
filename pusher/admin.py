from django.contrib import admin

# Register your models here.
from pusher.models import Account_Module, Destination_Module

admin.site.register(Account_Module)
admin.site.register(Destination_Module)