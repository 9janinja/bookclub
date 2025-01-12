from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Profile 
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