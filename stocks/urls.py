"""stocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Prox Stock Tracker API')

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('',include('stores.urls')),
    path('', include('inventory.urls')),
    path('',include('users.urls')),
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
    path('docs/', schema_view)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


