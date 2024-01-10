from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from services.abstract_models import TimeStampedModel


# Create your models here.


class FAQ(TimeStampedModel):
    question = models.CharField(
        max_length=255,
        verbose_name=_("Sual"),
    )
    answer = RichTextField(
        verbose_name=_("Cavab")
    )
    display_order = models.PositiveSmallIntegerField(
        verbose_name=_("Göstərilmə sırası")
    )
    is_active = models.BooleanField(
        verbose_name=_("Aktiv"),
        default=True
    )

    def __str__(self):
        if len(self.question) > 100:
            return f"{self.question[:100]}..."
        else:
            return self.question

    class Meta:
        ordering = ("display_order", "id")
        verbose_name = _("Tez-tez verilən sual")
        verbose_name_plural = _("Tez-tez verilən suallar")


class Contact(TimeStampedModel):
    name = models.CharField(
        verbose_name=_("Ad"),
        max_length=100
    )
    email = models.EmailField(
        verbose_name=_("E-poçt"),
        max_length=100
    )
    phone_number = models.CharField(
        verbose_name=_("Telefon nömrəsi"),
        max_length=50
    )
    message = models.TextField(
        verbose_name=_("Mesaj")
    )

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

    class Meta:
        verbose_name = _("Əlaqə")
        verbose_name_plural = _("Əlaqələr")


class Subscriber(TimeStampedModel):
    email = models.EmailField(
        verbose_name=_("E-poçt"),
        max_length=100,
        unique=True,
    )
    subscription_status = models.BooleanField(
        verbose_name=_("Abunə statusu"),
        default=True
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Abunə")
        verbose_name_plural = _("Abunələr")


class SiteInfo(TimeStampedModel):
    name = models.CharField(
        verbose_name=_("Ad"),
        max_length=100,
    )
    header_logo = models.ImageField(
        verbose_name=_("Header Logo"),
        upload_to="site_info/",
    )
    footer_logo = models.ImageField(
        verbose_name=_("Footer Logo"),
        upload_to="site_info/",
    )
    footer_slogan = models.TextField(
        verbose_name=_("Footer Slogan"),
        blank=True,
        null=True
    )
    favicon = models.ImageField(
        verbose_name=_("Favicon"),
        upload_to="site_info/",
    )
    email1 = models.EmailField(
        verbose_name=_("E-poçt 1"),
        max_length=100,
        blank=True,
        null=True
    )
    email2 = models.EmailField(
        verbose_name=_("E-poçt 2"),
        max_length=100,
        blank=True,
        null=True
    )
    phone_number1 = models.CharField(
        verbose_name=_("Telefon nömrəsi 1"),
        max_length=50,
        blank=True,
        null=True
    )
    phone_number2 = models.CharField(
        verbose_name=_("Telefon nömrəsi 2"),
        max_length=50,
        blank=True,
        null=True
    )
    whatsapp = models.CharField(
        verbose_name=_("Whatsapp"),
        max_length=50,
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name=_("Ünvan"),
        max_length=255,
        blank=True,
        null=True
    )
    map = models.TextField(
        verbose_name=_("Xəritə"),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Sayt məlumatı")
        verbose_name_plural = _("Sayt məlumatları")


class SocialMedia(TimeStampedModel):
    site_info = models.ForeignKey(
        "core.SiteInfo",
        on_delete=models.CASCADE,
        related_name="social_media_links",
        verbose_name=_("Sayt məlumatı"),
    )
    platform = models.CharField(
        verbose_name=_("Platform"),
        max_length=50,
        choices=[
            ("facebook", "Facebook"),
            ("instagram", "Instagram"),
            ("linkedin", "Linkedin"),
            ("tiktok", "Tiktok"),
            ("telegram", "Telegram"),
            # Add other social media platforms if needed
        ]
    )
    url = models.URLField(
        verbose_name=_("URL"),
        max_length=255
    )