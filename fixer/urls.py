# fixer/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from the fixer app

urlpatterns = [
    path('', views.index, name='index'),  # Home page route (text or file upload)
]