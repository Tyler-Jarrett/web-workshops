from django.db import models

# Create your models here.
class Item(models.Model):
    itemName = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    cost = models.FloatField()
    stockCount = models.IntegerField(default = 0)
    image = models.ImageField(default = 'shop/placeholder_product.jpeg', upload_to = 'shop/')

    def __str__(self):
        return self.itemName