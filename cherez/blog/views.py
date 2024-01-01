from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.http import JsonResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import BlogPost, BlogCategory


# Create your views here.


def blog_list_view(request):
    category_slug = request.GET.get("category")
    query = request.GET.get("query")

    blog_posts = BlogPost.objects.filter(
        is_active=True).order_by("-created_at")

    category = None

    if category_slug:
        category = get_object_or_404(
            BlogCategory, slug=category_slug, is_active=True)
        blog_posts = blog_posts.filter(category=category)

    if query:
        blog_posts = blog_posts.filter(title__icontains=query)

    # Pagination
    page_size = 10
    paginator = Paginator(blog_posts, page_size)
    page = request.GET.get("page", 1)

    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        raise Http404(_("Invalid page number."))
    except EmptyPage:
        raise Http404(_("Invalid page number."))

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        html_content = render_to_string(
            "blog/includes/_blog_posts_partial.html", {"blog_posts": blog_posts})

        has_next_page = blog_posts.has_next()

        return JsonResponse({"html_content": html_content, "has_next_page": has_next_page})

    context = {
        "blog_posts": blog_posts,
    }
    return render(request, "blog/blog.html", context)


def blog_detail_view(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug, is_active=True)

    latest_blog_posts = BlogPost.objects.filter(
        is_active=True).order_by("-created_at")[:5]
    blog_categories = BlogCategory.objects.filter(
        is_active=True).order_by("title")

    context = {
        "blog_post": blog_post,
        "latest_blog_posts": latest_blog_posts,
        "blog_categories": blog_categories
    }
    return render(request, "blog/blog-detail.html", context)
