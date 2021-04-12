from django.contrib import admin

# Register your models here.
from .models import Company

class CityAdmin(admin.ModelAdmin):
    list_display = ("name")

admin.site.register(Company)