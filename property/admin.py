from django.contrib import admin

from .models import Flat, FlatAdmin


admin.site.register(Flat, FlatAdmin)
