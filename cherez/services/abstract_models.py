from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Yaradılma vaxtı"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Yenilənmə vaxtı"),
        auto_now=True
    )

    class Meta:
        abstract = True
