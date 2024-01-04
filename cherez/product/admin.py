from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (
    ProductCategory,
    Product,
    ProductImage,
    Discount
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
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass
