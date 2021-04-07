from django.contrib import admin
from .models import People

class PeopleAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(People, PeopleAdmin)
