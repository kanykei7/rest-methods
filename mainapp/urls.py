from rest_framework.routers import DefaultRouter as DR

from mainapp.views import (ProductViewSet, CartViewSet, CartProductViewSet)

router = DR()

router.register('products', ProductViewSet, basename='products')
router.register('carts', CartViewSet, basename='carts')
router.register('cart_products', CartProductViewSet, basename='cart_products')

urlpatterns = []

urlpatterns += router.urls
