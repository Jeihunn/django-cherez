from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.http import JsonResponse

from .forms import ContactForm, SubscriberForm
from .models import (
    FAQ,
    Subscriber
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