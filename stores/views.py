from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Store
from .serializer import StoreSerializer
# Create your views here.
class StoresView(ListCreateAPIView):
    queryset =  Store.objects.all()
    serializer_class =  StoreSerializer

class StoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset =  Store.objects.all()
    serializer_class = StoreSerializer