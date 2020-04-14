from django.contrib import admin
from.import views
from django.urls import path


urlpatterns = [
    path('', views.index_view, name="index"),
    path('single_post_page/<int:id>/', views.post_page_view, name="post_page"),
    path('article_category/<name>/', views.category_page_view, name="category_page"),
    
    ]