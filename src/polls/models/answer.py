from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from polls.models import QuestionAnswerType
from utils.models import AbstractTimeTrackable


class Answer(AbstractTimeTrackable, models.Model):

    created_by = models.ForeignKey(
        User,
        verbose_name=_("Кем отвечен"),
        related_name='answers',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    question = models.ForeignKey(
        "polls.Question",
        verbose_name=_("Вопрос"),
        related_name='answers',
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        _("Ответ (при выборе \"Ответ текстом\""),
        blank=True,
        null=True,
    )
    choices = models.ManyToManyField(
        'polls.AnswerChoice',
        verbose_name=_("Ответы (при выборе \"Ответ с выбором варианта\""),
        blank=True
    )
    type = models.PositiveSmallIntegerField(
        verbose_name=_("Тип ответа"),
        choices=QuestionAnswerType.choices()
    )

    class Meta:
        verbose_name = _("Ответ")
        verbose_name_plural = _("Ответы")

    def __str__(self):
        return f'Опрос: {self.question.poll.name}, Вопрос: {self.question.text}, Тип ответа: {self.type}'
