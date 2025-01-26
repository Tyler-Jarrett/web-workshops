from django import path
from . import views

app_name = 'customers'
url_patterns = [
    path('register/', views.register, name = 'registration'),
]