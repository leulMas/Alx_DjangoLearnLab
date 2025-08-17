# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from taggit.forms import TagWidget


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']   # include tags field
        widgets = {
            'tags': TagWidget(attrs={           # 👈 use TagWidget
                'class': 'form-control',
                'placeholder': 'Add tags separated by commas',
            }),
            TagWidget()
        }

