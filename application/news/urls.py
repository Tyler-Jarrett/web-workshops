from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('list', views.list_news, name='list-news'),
    path('<int:article_id>', views.detail_news, name='detail-news'),
]