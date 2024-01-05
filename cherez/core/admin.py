from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TranslationAdmin

from .models import (
    FAQ,
    Contact,
    Subscriber,
    SiteInfo,
    SocialMedia
)


# Register your models here.


# ========== Inline ==========
class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1
    verbose_name = _("Sosial mediya")
    verbose_name_plural = _("Sosial mediyalar")
# ========== END Inline ==========


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
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

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'phone_number',
        'message',
        'created_at',
        'updated_at',
    )
    list_display_links = (
        'id',
        'name',
        "phone_number",
    )


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'created_at',
        'updated_at',
    )
    list_display_links = (
        'id',
        'email',
    )


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    inlines = [SocialMediaInline,]