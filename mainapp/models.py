from django.db import models
from django.db.models import Sum


class Product(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    articul = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user_name = models.CharField(max_length=127)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)
    delivery_address = models.CharField(max_length=127)

    def __str__(self):
        return self.user_name


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_products')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products')
    total_price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)

    @property
    def sum_product_price(self):
        return self.product.price * self.amount

    # def product_amount(self):
    #     return self.products.all().count()

    def __str__(self):
        return self.product.name
