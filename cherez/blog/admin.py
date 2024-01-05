from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (
    BlogPost,
    BlogCategory,
)


# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(TranslationAdmin):
    list_display = (
        "title",
        "slug",
        "is_active",
        "category",
        "created_at",
        "updated_at"
    )
    list_filter = ("is_active", "category")
    search_fields = ("title",)
    readonly_fields = ("slug",)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(BlogCategory)
class BlogCategoryAdmin(TranslationAdmin):
    list_display = ("title", "slug", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }