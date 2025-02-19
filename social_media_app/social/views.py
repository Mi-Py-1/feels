from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post, Feel

def home(request):
    posts = Post.objects.all()
    return render(request, 'social/home.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Post.objects.create(user=request.user, content=content)
        return redirect('home')
    return render(request, 'social/create_post.html')

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.content = request.POST.get('content')
        post.save()
        return redirect('home')
    return render(request, 'social/update_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'social/delete_post.html', {'post': post})

@login_required
def add_feel(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        Feel.objects.create(post=post, user=request.user, rating=rating)
        return redirect('home')
    return render(request, 'social/add_feel.html', {'post': post})
