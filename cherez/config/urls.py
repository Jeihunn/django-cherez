"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from blog.sitemaps import BlogListSitemap, BlogPostSitemap
from product.sitemaps import ProductListSitemap, ProductSitemap
from core.sitemaps import StaticViewsSitemap


sitemaps = {
    'static_views': StaticViewsSitemap,
    'blog_list': BlogListSitemap,
    'blog_post': BlogPostSitemap,
    'product_list': ProductListSitemap,
    'product': ProductSitemap,
}


urlpatterns = [
    # Rosetta
    re_path(r'^rosetta/', include('rosetta.urls')),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),
]


urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path("", include('core.urls')),
    path("", include('blog.urls')),
    path("", include('product.urls')),
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
