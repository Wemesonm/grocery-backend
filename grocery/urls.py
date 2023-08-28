"""
URL configuration for grocery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from core.api.viewsets import GroceryListViewSet
from categories.api.viewsets import CategoryViewSet
from items.api.viewsets import ItemViewSet
from brands.api.viewsets import BrandViewSet
from units.api.viewsets import UnitViewSet
from store.api.viewsets import StoreViewSet


router = routers.DefaultRouter()
router.register(r'groceryList', GroceryListViewSet)
router.register(r'store', StoreViewSet)
router.register(r'units', UnitViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
# router.register(r'',)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api_schema/', get_schema_view(title='API Schema', description= 'Guide for the REST API'), name='api_schema'),
]
