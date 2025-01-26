from django.urls import path
from . import views

app_name = 'customers'
urlpatterns = [
    path('register/', views.register, name = 'registration'),
    path('', views.register)
]