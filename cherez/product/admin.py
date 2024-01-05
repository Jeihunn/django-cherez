from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TranslationAdmin

from .models import (
    ProductCategory,
    Product,
    ProductImage,
    Discount,
    ProductAdditional
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
    pass


@admin.register(ProductAdditional)
class ProductAdditionalAdmin(TranslationAdmin):
    search_fields = ["title"]
    list_display = ["title", "parent"]
    list_display_links = list_display

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
