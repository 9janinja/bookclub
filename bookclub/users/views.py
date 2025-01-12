from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.
def home(request):
    return HttpResponse("Hello, BookClub!")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})   
