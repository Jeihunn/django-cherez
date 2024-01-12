from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy


class StaticViewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = "https"

    def items(self):
        return ['index_view', 'about_us_view', 'contact_us_view']

    def location(self, item):
        return reverse_lazy(item)
