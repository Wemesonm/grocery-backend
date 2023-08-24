from rest_framework.serializers import ModelSerializer
from items.models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id', 
            'name',
            'category',
            'brand',
            'unit',
            'stock_qty',
            'max_stock_qty',
            'min_stock_qty',
        )