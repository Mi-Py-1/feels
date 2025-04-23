from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Feel
from django.contrib import messages
from django.http import JsonResponse
from .forms import PostForm
from .forms import CustomUserCreationForm

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Order posts by newest first
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the posts for the current page
    return render(request, 'social/home.html', {'page_obj': page_obj})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'social/create_post.html', {'form': form})

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'social/update_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Allow deletion if the user is the owner of the post or an admin
    if request.user == post.user or request.user.role == 'admin':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this post.')
    return redirect('home')

@login_required
def add_feel(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')  # Ensure the rating is passed in the POST data
        if rating:
            feel, created = Feel.objects.get_or_create(
                post=post,
                user=request.user,
                defaults={'rating': rating}
            )
            if not created:
                # If the user already added a feel, update the rating
                feel.rating = rating
                feel.save()
                messages.success(request, 'Feel updated successfully!')
            else:
                messages.success(request, 'Feel added successfully!')
        else:
            messages.error(request, 'Rating is required to add a feel.')
    return redirect('home')

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