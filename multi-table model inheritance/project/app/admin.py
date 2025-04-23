from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
admin.site.register(student)
admin.site.register(employee)
# admin.site.register(client)