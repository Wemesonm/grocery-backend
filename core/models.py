from django.db import models
from items.models import Item
from django.contrib.auth.models import User


class Grocery(models.Model):
    name = models.CharField(max_length=10)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    qty = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    comments = models.TextField(max_length=200)
    get = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name




