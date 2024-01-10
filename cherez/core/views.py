from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.http import JsonResponse

from product.models import (
    ProductCategory,
    Product
)

from blog.models import (
    BlogPost,
)

from .forms import ContactForm, SubscriberForm
from .models import (
    FAQ,
    HomeAdvantage,
    HomeBanner
)


# Create your views here.


def index_view(request):
    home_product_categories = ProductCategory.objects.filter(show_in_home=True).order_by("-created_at")[:10]
    home_products = Product.objects.filter(show_in_home=True, is_active=True).order_by("-created_at")[:10]

    latest_blogs = BlogPost.objects.filter(is_active=True).order_by("-created_at")[:7]

    advertages = HomeAdvantage.objects.filter(is_active=True).order_by("-created_at")
    home_banner = HomeBanner.objects.first()

    context = {
        "home_product_categories": home_product_categories,
        "home_products": home_products,
        "latest_blogs": latest_blogs,
        "advertages": advertages,
        "home_banner": home_banner
    }
    return render(request, "core/index.html", context)


def about_us_view(request):
    faqs = FAQ.objects.filter(is_active=True).order_by("display_order")

    context = {
        "faqs": faqs,
    }
    return render(request, 'core/about-us.html', context)


def contact_us_view(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Mesaj uğurla göndərildi."))
            return redirect(reverse_lazy("contact_us_view"))
    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, 'core/contact-us.html', context)


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True}, status=200)
        else:
            email_errors = form.errors.get('email', [])
            return JsonResponse({'success': False, 'email_errors': email_errors})
    return JsonResponse({'message': _('Etibarsız sorğu!')}, status=400)