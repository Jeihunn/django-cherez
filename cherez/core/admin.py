from django.contrib import admin

from .models import FAQ


# Register your models here.


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question',
        'display_order',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_display_links = (
        'id',
        'question',
    )