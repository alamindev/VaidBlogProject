from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Author, Contact


admin.site.register(Author)

admin.site.register(Contact)
