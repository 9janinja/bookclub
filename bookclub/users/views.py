from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Profile, Book 
from django.contrib.auth.decorators import login_required

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
    return render(request, 'users/dashboard.html')

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
     
"""     profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegisterForm(instance=profile)
    return render(request, 'users/edit_profile.html', {'form': form}) """
    
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'users/book_list.html', {'books': books})    

@login_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        Book.objects.create(title=title, author=author, description=description, uploaded_by=request.user)  
        return redirect('book_list')
    
    return render(request, 'users/add_book.html')