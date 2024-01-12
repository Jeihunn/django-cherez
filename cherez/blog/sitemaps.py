from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy

from .models import BlogPost


class BlogPostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = "https"

    def items(self):
        return BlogPost.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse_lazy("blog_detail_view", kwargs={"slug": obj.slug})


class BlogListSitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = "https"

    def items(self):
        return ["blog_list_view"]

    def location(self, item):
        return reverse_lazy(item)
