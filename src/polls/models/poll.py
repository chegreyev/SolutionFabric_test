from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractTimeTrackable


class Poll(AbstractTimeTrackable,
           models.Model):

    name = models.CharField(
        _("Наименование"),
        max_length=256,
    )
    description = models.TextField(
        _("Описание")
    )
    date_start = models.DateField(
        _("Дата старта")
    )
    date_end = models.DateField(
        _("Дата окончания")
    )

    class Meta:
        verbose_name = _("Опрос")
        verbose_name_plural = _("Опросы")

    def __str__(self):
        return f'{self.name}'