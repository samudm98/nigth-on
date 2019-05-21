from nigth_on.products.models import Product
from django.contrib import admin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
