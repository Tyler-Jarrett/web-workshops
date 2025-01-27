from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm
from customers.models import StoreUser

# Create your views here.
def index(request):
    return render(request, 'shop/home.html')

def list_view(request):
    product_list = Item.objects.all()

    return render(request, 'shop/products.html', {'product_list': product_list})

def detail_view(request, item_id):
    product = Item.objects.get(pk = item_id)

    return render(request, 'shop/detail.html', {'product': product})

@login_required
def create_product(request):

    customer_account = StoreUser.objects.get(user__pk = request.user.id)
    if customer_account.role == 'admin':
        form = ItemForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('shop:product_list_view')
        
        return render(request, 'shop/product_form.html', {'form':form})
    return redirect('customers:access_denied')

@login_required
def edit_product(request, item_id):

    customer_account = StoreUser.objects.get(user__pk = request.user.id)
    if customer_account.role == 'admin':
        product = Item.objects.get(pk = item_id)
        form = ItemForm(request.POST or None, instance = product)

        if form.is_valid():
            form.save()
            return redirect('shop:product_list_view')
        
        return render(request, 'shop/product_form.html', {'form':form})
    return redirect('customers:access_denied')

@login_required
def delete_product(request, item_id):

    customer_account = StoreUser.objects.get(user__pk = request.user.id)
    if customer_account.role == 'admin':

        product = Item.objects.get(pk = item_id)

        if request.method == 'POST':
            product.delete()
            return redirect('shop:product_list_view')
        
        return render(request, 'shop/delete.html', {'product':product})
    return redirect('customers:access_denied')
    

