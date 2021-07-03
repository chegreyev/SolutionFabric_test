from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractTimeTrackable
from utils.const import Choice


class QuestionAnswerType(int, Choice):
    TEXT_ANSWER = 0      # _("Ответ текстом")
    SIMPLE_ANSWER = 1    # _("Ответ с выбором одного варианта")
    MULTIPLE_ANSWER = 2  # _("Ответ с выбором нескольких вариантов")


class Question(AbstractTimeTrackable, models.Model):
    poll = models.ForeignKey(
        'polls.Poll',
        verbose_name=_("Опрос"),
        related_name='questions',
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        _("Текст вопроса")
    )
    type = models.PositiveSmallIntegerField(
        _("Тип вопроса"),
        choices=QuestionAnswerType.choices(),
    )
    choices = models.ManyToManyField(
        'polls.AnswerChoice',
        verbose_name=_("Варианты ответа"),
        related_name='question',
    )

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")
        ordering = ['created_at']


class AnswerChoice(AbstractTimeTrackable, models.Model):
    text = models.TextField(
        _("Текст варианта ответа"),
    )

    class Meta:
        verbose_name = _("Вариант ответа")
        verbose_name_plural = _("Варианты ответа")
