from django import forms
from .models import Comments, Post
from django.forms import TextInput, DateTimeInput, Textarea

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text_comments', 'name', 'email')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'author', 'date')
        
        widgets = {
            "title": TextInput(attrs={'placeholder': 'Title'}),
            "description": Textarea(attrs={'placeholder': 'Description'}),
            "author": TextInput(attrs={'placeholder': 'Author'}),
            "date": DateTimeInput(attrs={'placeholder': 'Date'}),
        }
