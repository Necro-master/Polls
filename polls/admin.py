from django.contrib import admin
from .models import Answer, AnswerQuestion, AnswerChoice, Question, Poll, Choice

admin.site.register(Answer)
admin.site.register(AnswerChoice)
admin.site.register(AnswerQuestion)
admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(Choice)

# Register your models here.
