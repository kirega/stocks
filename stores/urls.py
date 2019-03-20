from django.urls import path
from .views import StoresView, StoresDetailView

urlpatterns = [
    path('stores/',StoresView.as_view(), name='stores'),
    path('stores/<pk>',StoresDetailView.as_view(), name='stores-detail'),
]
