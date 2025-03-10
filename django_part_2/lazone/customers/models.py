from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StoreUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    role = models.CharField(max_length=50, default='user')
    