from django.shortcuts import render

from .models import (
    FAQ,
)


# Create your views here.


def index_view(request):

    context = {

    }
    return render(request, "core/index.html", context)


def about_us_view(request):
    faqs = FAQ.objects.filter(is_active=True).order_by("display_order")

    context = {
        "faqs": faqs,
    }
    return render(request, 'core/about-us.html', context)


def contact_us_view(request):

    context = {

    }
    return render(request, "core/contact-us.html", context)