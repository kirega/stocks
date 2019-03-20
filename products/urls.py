from django.urls import path
from .views import ProductView, ProductDetailView
urlpatterns = [
    path('products/', ProductView.as_view(), name="products"),
    path('products/<pk>', ProductDetailView.as_view(), name="products-detail"),
]
