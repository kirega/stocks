from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Inventory
from .serializer import InventorySerializer, InventoryCreateSerializer
# Create your views here.
class InventoryView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class InventoryCreateView(CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryCreateSerializer
    permission_classes = (IsAuthenticated,)

class InventoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryCreateSerializer
    permission_classes = (IsAuthenticated,)
    