from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from mainapp.serializers import (Product, Cart, CartProduct, ProductSerializer, CartSerializer, CartProductSerializer)
from rest_framework import permissions


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartProductViewSet(ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
