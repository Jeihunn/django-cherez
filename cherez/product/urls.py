from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list_view, name="product_list_view"),
    path("product/<slug:slug>/", views.product_detail_view, name="product_detail_view"),
#     path("contact-us/", views.contact_us_view, name="contact_us_view"),
]