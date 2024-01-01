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
    logo = models.ImageField(
        verbose_name=_("Logo"),
        upload_to="site_info/",
    )
    favicon = models.ImageField(
        verbose_name=_("Favicon"),
        upload_to="site_info/",
    )
    email1 = models.EmailField(
        verbose_name=_("E-poçt 1"),
        max_length=100
    )
    email2 = models.EmailField(
        verbose_name=_("E-poçt 2"),
        max_length=100
    )
    phone_number1 = models.CharField(
        verbose_name=_("Telefon nömrəsi 1"),
        max_length=50
    )
    phone_number2 = models.CharField(
        verbose_name=_("Telefon nömrəsi 2"),
        max_length=50
    )
    address = models.CharField(
        verbose_name=_("Ünvan"),
        max_length=255
    )
    map = models.CharField(
        verbose_name=_("Xəritə"),
        max_length=255,
        blank=True,
        null=True
    )
    facebook_url = models.URLField(
        verbose_name=_("Facebook URL"),
        blank=True,
        null=True
    )
    whatsapp_url = models.URLField(
        verbose_name=_("Whatsapp URL"),
        blank=True,
        null=True
    )
    instagram_url = models.URLField(
        verbose_name=_("Instagram URL"),
        blank=True,
        null=True
    )
    linkedin_url = models.URLField(
        verbose_name=_("Linkedin URL"),
        blank=True,
        null=True
    )
    tiktok_url = models.URLField(
        verbose_name=_("Tiktok URL"),
        blank=True,
        null=True
    )
    telegram_url = models.URLField(
        verbose_name=_("Telegram URL"),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Sayt məlumatı")
        verbose_name_plural = _("Sayt məlumatları")