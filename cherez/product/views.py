from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import (
    Product,
    ProductCategory
)

# Create your views here.


def product_list_view(request):
    ordering = request.GET.get('ordering', '-created_at')

    products = Product.objects.filter(is_active=True).order_by(ordering)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 10)  # Show 10 products per page

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        raise Http404(_("Invalid page number."))
    except EmptyPage:
        raise Http404(_("Invalid page number."))

    parent_categories = ProductCategory.objects.filter(parent__isnull=True)

    context = {
        'products': products,
        'current_ordering': ordering,
        'parent_categories': parent_categories
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
