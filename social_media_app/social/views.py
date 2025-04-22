from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Feel
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Order posts by newest first
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the posts for the current page
    return render(request, 'social/home.html', {'page_obj': page_obj})

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
        messages.success(request, 'Post created successfully!')
        return redirect('home')
    return render(request, 'social/create_post.html')

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.content = request.POST.get('content')
        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('home')
    return render(request, 'social/update_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')
    return render(request, 'social/delete_post.html', {'post': post})

@login_required
def add_feel(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        Feel.objects.create(post=post, user=request.user, rating=rating)
        if created:
            messages.success(request, 'Your feel has been added to the post!')
        else:
            messages.info(request, 'You have already added a feel to this post.')
        return redirect('home')
    return render(request, 'social/add_feel.html', {'post': post})

def custom_logout(request):
    auth_logout(request)
    return redirect('/?show_logout_modal=true')

@login_required
def notifications(request):
    # Example notifications (replace with your logic)
    notifications = [
        {"message": "New post created!", "tag": "success"},
        {"message": "You have a new feel!", "tag": "info"},
    ]
    return JsonResponse({"notifications": notifications})