from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TranslationAdmin

from .models import (
    ProductCategory,
    Product,
    ProductImage,
    Discount,
    ProductAdditional,
)


# Register your models here.


# ========== Inline ==========
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    verbose_name = _("Şəkil")
    verbose_name_plural = _("Şəkillər")
# ========== END Inline ==========


@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = (
        'id',
        'title',
        'parent',
        'show_in_navbar',
        'show_in_footer',
        'show_in_home',
        'slug',
        'created_at',
        'updated_at',
    )
    list_display_links = list_display
    search_fields = ['title', 'slug']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImageInline,]
    autocomplete_fields = ["additionals"]

    list_display = (
        'id',
        'product_code',
        'title',
        'slug',
        'category',
        'price',
        'discount',
        'weight',
        'is_new',
        'show_in_home',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_display_links = list_display
    search_fields = ['title', 'product_code', 'slug']
    list_filter = ['is_active', 'is_new', 'show_in_home']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'percent',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_display_links = list_display
    search_fields = ['title']
    list_filter = ['is_active']


@admin.register(ProductAdditional)
class ProductAdditionalAdmin(TranslationAdmin):
    list_display = (
        'id',
        'title',
        'parent',
        'slug',
        'created_at',
        'updated_at',
    )
    list_display_links = list_display
    search_fields = ['title', 'slug']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
