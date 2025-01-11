from django.shortcuts import render, redirect
from .models import Item
from .form import ItemForm

# Create your views here.
def index(request):
    return render(request, 'shop/home.html')

def list_view(request):
    product_list = Item.objects.all()

    return render(request, 'shop/products.html', {'product_list': product_list})

def detail_view(request, item_id):
    product = Item.objects.get(pk = item_id)

    return render(request, 'shop/detail.html', {'product': product})

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('shop:product_list_view')
    
    return render(request, 'shop/product_form.html', {'form':form})

def edit_product(request, item_id):
    product = Item.objects.get(pk = item_id)
    form = ItemForm(request.POST or None, instance = product)

    if form.is_valid():
        form.save()
        return redirect('shop:product_list_view')
    
    return render(request, 'shop/product_form.html', {'form':form})

def delete_product(request, item_id):
    product = Item.objects.get(pk = item_id)

    if request.method == 'POST':
        product.delete()
        return redirect('shop:product_list_view')
    
    return render(request, 'shop/delete.html', {'product':product})
    

