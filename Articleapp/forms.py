from django import forms
from django.contrib.auth import get_user_model 
from .models import Comment

User = get_user_model()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'comment', 

            ]