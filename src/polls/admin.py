from django.contrib import admin

from polls.models import Poll, Question, Answer, AnswerChoice


admin.site.register(Poll)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(AnswerChoice)
