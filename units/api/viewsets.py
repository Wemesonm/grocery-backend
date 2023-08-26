from rest_framework.viewsets import ModelViewSet
from units.models import Unit
from .serializers import UnitSerializer

class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer