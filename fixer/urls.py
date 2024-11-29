# fixer/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from the fixer app

urlpatterns = [
    path('', views.index, name='index'),  # Home page route (text or file upload)
    path('page-one/', views.page_one, name='page_one'),
    path('page-two/', views.page_two, name='page_two'),

]
