from django.urls import path
from product.views import product_view, test_view

app_name = 'product'

urlpatterns = [
    path('', product_view, name='product-home'),
    path('test/', test_view, name='test-view'),
]