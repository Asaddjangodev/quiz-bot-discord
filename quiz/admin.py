from django.contrib import admin

from .models import Question, Answer
# Register your models here.


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        "answer",
        "is_correct",
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "points",
        "difficulty",
    ]
    list_display = [
        "title",
        "updated_at",
    ]
    inlines = [
        AnswerInlineModel,
    ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = [
        "answer",
        "is_correct",
        "question",
]
