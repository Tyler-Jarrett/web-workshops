from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegistrationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'customers/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('customers:login')

def access_denied(request):
    return render(request, 'customers/denied.html')