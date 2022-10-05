from django.contrib import admin

from mainapp.models import (
    Product, Cart, CartProduct
)

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
