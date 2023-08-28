from rest_framework.viewsets import ModelViewSet
from core.models import Grocery
from .serializers import GroceryListSerializer

class GroceryListViewSet(ModelViewSet):
    queryset = Grocery.objects.all()
    serializer_class = GroceryListSerializer