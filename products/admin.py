from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'category',
        'description',
        'country',
        'region',
        'grape',
        'vintage',
    )

    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
     list_display = (
        'friendly_name',
        'name'
,     )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)