from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.blog_list_view, name="blog_list_view"),
    path("blog/<slug:slug>/", views.blog_detail_view, name="blog_detail_view"),
]
