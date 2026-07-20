from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import StoreUser

@receiver(post_save, sender = User)
def build_store_user(sender, instance, created, **kwargs):
    if created:
        StoreUser.objects.create(user = instance)
    instance.storeuser.save()