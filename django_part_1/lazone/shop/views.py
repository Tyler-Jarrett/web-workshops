from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shop/home.html')

def list_view(request):
    return render(request, 'home.html')