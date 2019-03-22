from rest_framework import serializers
from .models import Inventory
from products.serializer import ProductSerializer
from products.models import Product
from stores.serializer import StoreSerializer
from stores.models import Store
class InventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventory
        fields = ('id', 'store', 'product', 'quantity')
        depth = 1
        
class InventoryCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventory
        fields = ('id', 'store', 'product', 'quantity')
