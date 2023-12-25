from django.contrib import admin

from .models import (
    BlogPost,
    BlogCategory,
)


# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
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


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)