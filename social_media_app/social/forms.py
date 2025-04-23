from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your post here...',
                'rows': 4,
            }),
        }
        labels = {
            'content': 'Post Content',
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or content.strip() == "":
            raise forms.ValidationError("Content cannot be empty.")
        if len(content) > 500:
            raise forms.ValidationError("Content cannot exceed 500 characters.")
        return content