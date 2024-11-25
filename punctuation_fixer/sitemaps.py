# sitemaps.py
from django.contrib.sitemaps import Sitemap

class StaticSitemap(Sitemap):
    def items(self):
        # Since you have a one-page site, just add the homepage URL
        return ['/']

    def location(self, item):
        return item
