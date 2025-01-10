from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.list_view, name = 'product_list_view'),
    path('<int:item_id>/', views.detail_view, name = 'product_detail_view'),
]