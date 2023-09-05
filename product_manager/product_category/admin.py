from django.contrib import admin

from .models import ProductCategoryModel


# Register your models here.
@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name']
