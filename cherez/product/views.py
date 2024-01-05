from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import (
    Product,
    ProductCategory,
    ProductAdditional
)

# Create your views here.


def product_list_view(request):
    # Default ordering is by creation time in descending order
    ordering = request.GET.get('ordering', '-created_at')

    # Filter products based on user input
    products = Product.objects.filter(is_active=True).order_by(ordering)

    # Search by query if provided
    query = request.GET.get("query")
    if query:
        products = products.filter(title__icontains=query)

    # Filter by price range
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Filter by selected categories
    selected_categories = request.GET.getlist('category')
    if selected_categories:
        products = products.filter(category__slug__in=selected_categories)

    # Filter by selected additionals
    selected_additionals = request.GET.getlist('additional')
    if selected_additionals:
        products = products.filter(additionals__slug__in=selected_additionals)

    # Use distinct to ensure each product is unique
    products = products.distinct()

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 10)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        raise Http404(_("Invalid page number."))
    except EmptyPage:
        raise Http404(_("Invalid page number."))

    parent_null_categories = ProductCategory.objects.filter(
        parent__isnull=True)
    parent_null_additionals = ProductAdditional.objects.filter(
        parent__isnull=True)

    context = {
        'products': products,
        'parent_null_categories': parent_null_categories,
        'parent_null_additionals': parent_null_additionals,
        'current_ordering': ordering,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'selected_additionals': selected_additionals,
        'selected_categories': selected_categories,
    }

    return render(request, 'product/products.html', context)


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    similar_products = Product.objects.filter(
        category=product.category,
        is_active=True,
    ).exclude(
        id=product.id
    ).order_by("-created_at")[:8]

    context = {
        "product": product,
        "similar_products": similar_products,
    }
    return render(request, "product/product-details.html", context)
