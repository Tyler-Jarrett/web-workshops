from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    creation_time = models.TimeField(auto_now_add=True)
    last_update_date = models.DateField()
    last_update_time = models.TimeField()
    title = models.CharField()
    image = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)
    category = models.CharField()

class Section(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    heading = models.CharField()
    text = models.CharField()
    order = models.IntegerField()
