from django import forms
from .models import Blogs, Posts

class BlogsForm(forms.ModelForm):
    """create blog form"""
    class Meta:
        model = Blogs
        fields = ['blog']
        labels = {'blog': ''}

class PostsForm(forms.ModelForm):
    """create post form"""
    class Meta:
        model = Posts
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
