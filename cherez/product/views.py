from django.shortcuts import render, get_object_or_404

from .models import (
    Product,
    ProductCategory
)

# Create your views here.


def product_list_view(request):
    ordering = request.GET.get('ordering', '-created_at')

    products = Product.objects.filter(is_active=True).order_by(ordering)

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