from django.test import TestCase
from django.urls import reverse
from .models import Post, CustomUser, Feel
from .forms import PostForm


# Test cases for the social media app
class PostModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(user=self.user, content="Test content")

    def test_post_creation(self):
        self.assertEqual(self.post.content, "Test content")
        self.assertEqual(self.post.user.username, "testuser")


class PostViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.post = Post.objects.create(user=self.user, content="Test content")

    def test_signup_view(self):
        # Test successful signup
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(username='newuser').exists())

        # Test signup with mismatched passwords
        response = self.client.post(reverse('signup'), {
            'username': 'newuser2',
            'password1': 'password123',
            'password2': 'password456'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The two password fields didn’t match.")
        self.assertFalse(CustomUser.objects.filter(username='newuser2').exists())

    def test_add_feel_view(self):
        post = Post.objects.create(user=self.user, content="Test post")

        # Test adding a new feel
        response = self.client.post(reverse('add_feel', args=[post.id]), {'rating': 5})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Feel.objects.filter(post=post, user=self.user, rating=5).exists())

        # Test updating an existing feel
        response = self.client.post(reverse('add_feel', args=[post.id]), {'rating': 3})
        self.assertEqual(response.status_code, 302)
        feel = Feel.objects.get(post=post, user=self.user)
        self.assertEqual(feel.rating, 3)

        # Test adding feel with missing rating
        response = self.client.post(reverse('add_feel', args=[post.id]), {})
        self.assertEqual(response.status_code, 302)

    def test_delete_profile_view(self):
        # Test successful profile deletion
        response = self.client.post(reverse('delete_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CustomUser.objects.filter(username=self.user.username).exists())

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test content")

    def test_post_create_view(self):
        response = self.client.post(reverse('create_post'), {'content': 'New post content'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Post.objects.filter(content="New post content").exists())

    def test_post_update_view(self):
        response = self.client.post(reverse('update_post', args=[self.post.id]), {'content': 'Updated content'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.post.refresh_from_db()
        self.assertEqual(self.post.content, 'Updated content')

    def test_post_delete_view(self):
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_notifications_view(self):
        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.status_code, 200)
    
        # Parse the JSON response
        data = response.json()
    
        # Check that the response contains the expected notifications
        self.assertIn("notifications", data)
        self.assertEqual(len(data["notifications"]), 2)  # Ensure there are 2 notifications
        self.assertEqual(data["notifications"][0]["message"], "New post created!")
        self.assertEqual(data["notifications"][1]["message"], "You have a new feel!")

    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 302)  # Redirect to login


class PostFormTest(TestCase):
    def test_valid_form(self):
        form = PostForm(data={'content': 'Valid content'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = PostForm(data={'content': ''})  # Empty content
        self.assertFalse(form.is_valid())
