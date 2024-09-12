from django.contrib import admin
from .models import Bird

# Register your models here.

@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'description') 