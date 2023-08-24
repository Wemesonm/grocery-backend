from django.db import models
from categories.models import Category
from brands.models import Brand
from units.models import Unit


class Item(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    stock_qty = models.IntegerField()
    max_stock_qty = models.IntegerField()
    min_stock_qty = models.IntegerField()
    
    def __str__(self):
        return self.name