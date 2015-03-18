from django.contrib import admin
from .models import CatProductCategory # , CatProductCategoryChild

class CatProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'primary', 'parent']

# class CatProductCategoryChildAdmin(admin.ModelAdmin):
#     list_display = ['categoryParent', 'categoryChild']

admin.site.register( CatProductCategory, CatProductCategoryAdmin )
# admin.site.register( CatProductCategoryChild, CatProductCategoryChildAdmin )