from rest_framework.generics import ListAPIView, CreateAPIView
from .serializer import UserSerializer , UserCreateSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth.models import User

class UserListView(ListAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

class UserCreateView(CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)
