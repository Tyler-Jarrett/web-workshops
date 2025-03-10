from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('itemName', 'price', 'cost', 'stockCount')

admin.site.register(Item, ItemAdmin)