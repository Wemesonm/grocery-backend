from rest_framework.serializers import ModelSerializer
from core.models import Grocery

class GroceryListSerializer(ModelSerializer):
    class Meta:
        model = Grocery
        fields = '__all__'