from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from ckeditor.fields import RichTextField

from services.abstract_models import TimeStampedModel
from services.utils import create_unique_slug


# Create your models here.


class BlogCategory(TimeStampedModel):
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=255,
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

    def __str__(self):
        if len(self.title) > 100:
            return f"{self.title[:100]}..."
        else:
            return self.title

    class Meta:
        verbose_name = _("Bloq Kategoriyası")
        verbose_name_plural = _("Bloq Kateqoriyaları")


class BlogPost(TimeStampedModel):
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=255,
    )
    page_title = models.CharField(
        verbose_name=_("Səhifə başlığı"),
        max_length=255,
        null=True,
        blank=True
    )
    page_description = models.TextField(
        verbose_name=_("Səhifə açıqlaması"),
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        to="blog.BlogCategory",
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        verbose_name=_("Bloq Kateqoriyası"),
    )
    short_description = models.TextField(
        verbose_name=_("Qısa məzmun"),
        max_length=255
    )
    content = RichTextField(
        verbose_name=_("Məzmun")
    )
    cover_image = models.ImageField(
        verbose_name=_("Cover şəkili"),
        upload_to="blog/cover_images/",
    )
    detail_image = models.ImageField(
        verbose_name=_("Məzmun şəkili"),
        upload_to="blog/detail_images/",
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name=_("Aktiv"),
        default=True
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        editable=False,
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
        if len(self.title) > 100:
            return f"{self.title[:100]}..."
        else:
            return self.title

    class Meta:
        verbose_name = _("Bloq")
        verbose_name_plural = _("Bloqlar")