from django.contrib import admin
from .models import ProductFeatures

class ProductFeaturesAdmin(admin.ModelAdmin):
    list_display = ['feature']

admin.site.register( ProductFeatures, ProductFeaturesAdmin )
