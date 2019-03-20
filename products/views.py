from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)