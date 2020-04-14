from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('author_post_page/<name>/', views.author_post_view, name="author_post"),
    path('article_create/', views.article_create_view, name="article_create"),
    path('author_profile/', views.author_profile_view, name="author_profile"),
    path('login_page/', views.login_view, name="login"),
    path('logout_page/', views.logout_view, name="logout"),
    path('register_page/', views.register_view, name="register_page") ,
    #path('activate/<uidb64>/<token>/', views.activate_view, name="activate"),

    ]