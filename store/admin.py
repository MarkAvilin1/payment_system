from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'added_at', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'quantity', 'is_available')


admin.site.register(Product, ProductAdmin)
