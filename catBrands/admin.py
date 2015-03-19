from django.contrib import admin
from .models import CatBrand

class CatBrandAdmin(admin.ModelAdmin):
    list_display = ['brand', 'web']

admin.site.register( CatBrand, CatBrandAdmin )
