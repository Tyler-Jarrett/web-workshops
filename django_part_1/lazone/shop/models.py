from django.db import models

# Create your models here.
class Item(models.Model):
    itemName = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    cost = models.FloatField()
    stockCount = models.IntegerField()

    def __str__(self):
        return self.itemName