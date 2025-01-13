from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Profile
from books.models import Book

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

@login_required
def dashboard(request):
    user_books = Book.objects.filter(uploaded_by=request.user)  
    return render(request, 'users/dashboard.html', {'user_books': user_books})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        bio = request.POST['bio']
        favorite_genre = request.POST['favorite_genre']
        request.user.profile.bio = bio
        request.user.profile.favorite_genre = favorite_genre    
        request.user.profile.save()
        return redirect('dashboard')    
    return render(request, 'users/edit_profile.html', {'profile': request.user.profile})