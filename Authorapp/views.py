from django.shortcuts import render, redirect,HttpResponse,get_object_or_404,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.core.mail import send_mail
from.forms import registerUserForm, ArticleCreateForm, ProfileForm
from django.contrib.auth.views import LoginView
from .models import Author, Contact
from Articleapp.models import Article
from django.contrib import messages
from django.urls import reverse_lazy

User = get_user_model() 


def author_post_view(request, name):
    author_post = get_object_or_404(User, username=name)
    auth = get_object_or_404(Author, name=author_post.id)
    author_article_post = Article.objects.filter(author_id=auth.id)
    context = {
            'auth':auth,
            'author_article_post':author_article_post,
        }
    return render(request, "accounts/author_post_page.html", context)


def article_create_view(request): 
    if request.user.is_authenticated:
        user = get_object_or_404(Author, name=request.user.id)
        form = ArticleCreateForm(request.POST or None, request.FILES or None)
        if form .is_valid():
            instance = form.save(commit=False)
            instance.author_id = user
            instance.save()
            messages.success(request, "Article successfully create")
            return redirect("index")  
        return render(request, "accounts/articlecreate.html",{"form":form})
    else:
        return redirect("login")    

def author_profile_view(request):
    if request.user.is_authenticated:
        authorprofile = get_object_or_404(Author, name=request.user.id)
        authorallarticle = Article.objects.filter(author_id= authorprofile.id)
        context = {
            'authorallarticle': authorallarticle,
            'authorprofile':authorprofile,
        }
        return render(request, "accounts/profile.html", context)
    else:
      return redirect("login")    


def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            user        = request.POST.get('user')
            password    = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            
            if auth is not None:
                login(request, auth)
                messages.success(request, "Login successfully")
                return redirect("index")
            else:
                messages.warning(request, "Password Incorrect")        
    return render(request, "accounts/login-page.html") 

 
def logout_view(request):
    messages.success(request, 'Logout Successfully')
    logout(request)
    return redirect("index")



def register_view(request):
    registered = False
    if request.method=='POST':
        form = registerUserForm(request.POST or None)
        profile_form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            profile_user = profile_form.save(commit=False)
            profile_user.name = user

            if 'profile_image' in request.FILES:
                profile_user.profile_image = request.FILES['profile_image']
            profile_user.save()
            registered = True
            messages.success(request, " SignUp Successfully")
            
            return redirect('index')
        else:
            messages.warning(request, " Username already exists")
            print(form.errors, profile_form.errors)        
    else:
        form = registerUserForm()
        profile_form = ProfileForm()        
    context ={
        'form':form,
        'profile_form':profile_form,
        'registered':registered
        
        }    
    return render(request, 'accounts/register-page.html', context)  





