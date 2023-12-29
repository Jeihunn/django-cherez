from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from services.abstract_models import TimeStampedModel
from services.utils import create_unique_slug


# Create your models here.


class ProductCategory(TimeStampedModel):
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="sub_categories",
        verbose_name=_("Üst Kategoriyası"),
    )
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=255
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        editable=False
    )

    def clean(self):
        # Generate a unique slug if it's not set
        if not self.slug:
            try:
                self.slug = create_unique_slug(
                    self, "title", empty_error_msg=_("Slug dəyəri boş ola bilməz. Başlığı düzəldin.")
                )
            except ValueError as e:
                raise ValidationError(str(e))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        result = ""
        if len(self.title) > 100:
            result = f"{self.title[:100]}..."
        else:
            result = self.title
        if self.parent:
            result += f" - [{self.parent}]"

        return result

    class Meta:
        verbose_name = _("Məhsul Kategoriyası")
        verbose_name_plural = _("Məhsul Kategoriyaları")


class Product(TimeStampedModel):
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=255
    )
    category = models.ForeignKey(
        to="product.ProductCategory",
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("Məhsul Kategoriyası"),
    )
    price = models.DecimalField(
        verbose_name=_("Qiymət"),
        max_digits=10,
        decimal_places=2
    )
    discount = models.ForeignKey(
        to="product.Discount",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name=_("Endirim"),
    )
    weight = models.FloatField(
        verbose_name=_("Çəki"),
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name=_("Açıqlama"),
    )
    cover_image = models.ImageField(
        verbose_name=_("Cover şəkili"),
        upload_to="product/cover_images/",
    )
    is_new = models.BooleanField(
        verbose_name=_("Yeni"),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_("Aktiv"),
        default=True
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        editable=False
    )

    def clean(self):
        # Generate a unique slug if it's not set
        if not self.slug:
            try:
                self.slug = create_unique_slug(
                    self, "title", empty_error_msg=_("Slug dəyəri boş ola bilməz. Başlığı düzəldin.")
                )
            except ValueError as e:
                raise ValidationError(str(e))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def discounted_price(self):
        if not self.discount:
            return None
        return self.price - (self.price * self.discount.percent / 100)
    
    @property
    def active_images(self):
        return self.images.filter(is_active=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Məhsul")
        verbose_name_plural = _("Məhsullar")


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(
        to="product.Product",
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Məhsul"),
    )
    image = models.ImageField(
        verbose_name=_("Şəkil"),
        upload_to="product/images/",
    )
    is_active = models.BooleanField(
        verbose_name=_("Aktiv"),
        default=True
    )

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = _("Məhsul Şəkili")
        verbose_name_plural = _("Məhsul Şəkilləri")


class Discount(TimeStampedModel):
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=50,
        unique=True
    )
    percent = models.PositiveSmallIntegerField(
        verbose_name=_("Faiz"),
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)]
    )
    is_active = models.BooleanField(
        verbose_name=_("Aktiv"),
        default=True
    )

    class Meta:
        verbose_name = _("Endirim")
        verbose_name_plural = _("Endirimlər")

    def __str__(self):
        return f"{self.title} - ({self.percent}%)"
