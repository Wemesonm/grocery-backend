from rest_framework.viewsets import ModelViewSet
from brands.models import Brand
from .serializers import BrandSerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
