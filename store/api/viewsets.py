from rest_framework.viewsets import ModelViewSet
from store.models import Store
from .serializers import StoreSerializer

class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
