# punctuation_fixer/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fixer.urls')),  # Include the app-level URLs from the 'fixer' app
]