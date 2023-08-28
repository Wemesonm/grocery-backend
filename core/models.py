from django.db import models
from items.models import Item
from store.models import Store
from django.contrib.auth.models import User


class Grocery(models.Model):
    name = models.CharField(max_length=10)
    item = models.ForeignKey(Item, on_delete=models.PROTECT, null=True, blank=True)
    qty = models.IntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.PROTECT, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    comments = models.TextField(max_length=200, null=True, blank=True)
    get = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
