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