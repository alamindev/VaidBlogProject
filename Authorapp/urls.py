from django.contrib import admin
from django.urls import path
from.import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('author_post_page/<name>/', views.author_post_view, name="author_post"),
    path('article_create/', views.article_create_view, name="article_create"),
    path('author_profile/', views.author_profile_view, name="author_profile"),
    path('login_page/', views.login_view, name="login"),
    path('logout_page/', views.logout_view, name="logout"),
    path('register_page/', views.register_view, name="register_page") ,
    #path('activate/<uidb64>/<token>/', views.activate_view, name="activate"),
    path('change-password/', auth_views.PasswordChangeView.as_view(
    	success_url=reverse_lazy('index'),
    	template_name="registration/password_change_form.html"),  
    	name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password/reset/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        post_reset_login= True,
        post_reset_login_backend='django.contrib.auth.backends.ModelBackend',
        template_name="registration/password_reset_confirm.html"),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_change_done.html"), name="password_reset_complete")
     

    ]