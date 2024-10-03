from django.contrib import admin
from .models import *

admin.site.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name')
    fields = ('name')
    search_fields = ('name')
    ordering = ('name')

admin.site.register(Kitten)

