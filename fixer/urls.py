# fixer/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from the fixer app

urlpatterns = [
    path('', views.index, name='index'),  # Home page route (text or file upload)
    path('stavekontrol/', views.stavekontrol, name='stavekontrol'),  # Add this line
    path('home/', views.home, name='home'),  # Corrected line
    path('policy/', views.policy, name='policy'),


]
