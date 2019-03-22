from django.urls import path
from .views import InventoryView, InventoryDetailView, InventoryCreateView

urlpatterns = [
    path('inventory/',InventoryView.as_view(), name='inventory'),
    path('inventory/create/',InventoryCreateView.as_view(), name='inventory-create'),
    path('inventory/<pk>',InventoryDetailView.as_view(), name='inventory-detail'),
]
