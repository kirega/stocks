from django.urls import path
from .views import InventoryView, InventoryDetailView

urlpatterns = [
    path('inventory/',InventoryView.as_view(), name='inventory'),
    path('inventory/<pk>',InventoryDetailView.as_view(), name='inventory-detail'),
]
