from rest_framework.serializers import ModelSerializer
from units.models import Unit

class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name')
