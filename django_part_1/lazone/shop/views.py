from django.shortcuts import render
from .models import Item

# Create your views here.
def index(request):
    return render(request, 'shop/home.html')

def list_view(request):
    product_list = Item.objects.all()

    return render(request, 'shop/products.html', {'product_list': product_list})