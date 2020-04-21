from django import forms
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Articleapp.models import Article, Category, Comment
from .models import Author

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
           'profile_image',
           'about',
        ]
            


class registerUserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]


class  ArticleCreateForm(forms.ModelForm):
    class  Meta:
        model = Article
        fields = [
            'title',
            'image',
            'description',
            'category_name',

        ]

