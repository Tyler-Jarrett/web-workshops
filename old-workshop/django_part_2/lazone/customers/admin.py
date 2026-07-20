from django.contrib import admin
from .models import StoreUser

# Register your models here.
class StoreUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

admin.site.register(StoreUser, StoreUserAdmin)
