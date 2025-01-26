from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'customers'
urlpatterns = [
    path('register/', views.register, name = 'registration'),
    path('', views.register),
    path('login/', auth_views.LoginView.as_view(template_name = 'customers/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'customers/logout.html'), name = 'logout'),
]