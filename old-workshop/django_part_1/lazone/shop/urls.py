from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.list_view, name = 'product_list_view'),
    path('<int:item_id>/', views.detail_view, name = 'product_detail_view'),
    path('add/', views.create_product, name = 'create_product'),
    path('edit/<int:item_id>', views.edit_product, name = 'edit_product'),
    path('delete/<int:item_id>', views.delete_product, name = 'delete_product')
]