from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

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
    url = models.URLField(
        verbose_name=_("URL"),
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


class HomeAdvantage(TimeStampedModel):
    icon_class = models.CharField(
        verbose_name=_("Ikon class"),
        max_length=50,
        help_text=_('Məs: "ti-headphone-alt" | class="CLASS_NAME"')
    )
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=100
    )
    description = models.TextField(
        verbose_name=_("Açıqlama"),
    )
    is_active = models.BooleanField(
        verbose_name=_("Aktiv"),
        default=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Avantaj")
        verbose_name_plural = _("Avantajlar")


class HomeBanner(TimeStampedModel):
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=100
    )
    description = models.TextField(
        verbose_name=_("Açıqlama"),
    )
    image = models.ImageField(
        verbose_name=_("Şəkil"),
        upload_to="home_banner/",
    )
    background_image = models.ImageField(
        verbose_name=_("Arxa plan şəkli"),
        upload_to="home_banner/",
    )
    link = models.URLField(
        verbose_name=_("Link"),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Ana səhifə banneri")
        verbose_name_plural = _("Ana səhifə banneri")

    def clean(self):
        existing_count = HomeBanner.objects.exclude(id=self.id).count()

        if existing_count > 0:
            raise ValidationError(
                _("Yalnız bir 'Ana səhifə banneri' olmalıdır. Artıq 1 ədəd banner mövcuddur."))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class HomeSlider(TimeStampedModel):
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=100
    )
    description = models.TextField(
        verbose_name=_("Açıqlama"),
    )
    image = models.ImageField(
        verbose_name=_("Şəkil"),
        upload_to="home_slider/",
    )
    button_text = models.CharField(
        verbose_name=_("Button mətni"),
        max_length=100,
        blank=True,
        null=True
    )
    button_link = models.URLField(
        verbose_name=_("Button linki"),
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name=_("Aktiv"),
        default=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Ana səhifə slayderi")
        verbose_name_plural = _("Ana səhifə slayderləri")


class AboutUs(TimeStampedModel):
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=100
    )
    description = models.TextField(
        verbose_name=_("Açıqlama"),
    )
    image = models.ImageField(
        verbose_name=_("Şəkil"),
        upload_to="about_us/",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Haqqımızda")
        verbose_name_plural = _("Haqqımızda")

    def clean(self):
        existing_count = AboutUs.objects.exclude(id=self.id).count()

        if existing_count > 0:
            raise ValidationError(
                _("Yalnız bir Haqqımızda məlumatı olmalıdır. Artıq 1 ədəd mövcuddur."))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class TitleDescription(TimeStampedModel):
    PAGE_CHOICES = (
        ("home", _("Ana səhifə")),
        ("about", _("Haqqımızda")),
        ("products", _("Məhsullar")),
        ("blogs", _("Bloqlar")),
        ("contact", _("Bizimlə əlaqə")),
    )

    page_type = models.CharField(
        verbose_name=_("Səhifə tipi"),
        max_length=50,
        unique=True,
        choices=PAGE_CHOICES
    )
    title = models.CharField(
        verbose_name=_("Başlıq"),
        max_length=400
    )
    description = models.TextField(
        verbose_name=_("Açıqlama"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Başlıq və Açıqlama")
        verbose_name_plural = _("Başlıq və Açıqlama")
