# punctuation_fixer/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap
from . import views  # Import views from the same app

sitemaps = {
    'static': StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fixer.urls')),  # Include the app-level URLs from the 'fixer' app
    path('stavekontrol/', views.stavekontrol, name='stavekontrol'),  # Add this line
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
