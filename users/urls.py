from django.urls import path
from .views import UserCreateView,UserListView

urlpatterns = [
    path('signup/', UserCreateView.as_view()),
    path('users/', UserListView.as_view())
]