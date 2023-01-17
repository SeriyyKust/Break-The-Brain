from django.contrib import admin
from .models import BaseQuestion, ElementQuestion, TextAnswer, ChoiceAnswer, Task


class ElementQuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "photo", "category")
    list_display_links = ("title", )
    search_fields = ("title", )
    list_editable = ("photo", "category")


class BaseQuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "question", "date", "cost", "slug")
    list_display_links = ("title", )
    search_fields = ("title", )
    list_editable = ("question", "cost", "slug")


class TextAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "correct_answer", )
    list_editable = ("correct_answer", )


class ChoiceAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "correct_answer", "wrong_answer_1", "wrong_answer_2", "wrong_answer_3")
    list_editable = ("correct_answer", "wrong_answer_1", "wrong_answer_2", "wrong_answer_3")


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "photo", "complexity", "owner", "questions_task", "slug")
    list_display_links = ("title", )
    search_fields = ("title", )
    list_editable = ("photo", "complexity", "owner", "slug")

    def questions_task(self, obj):
        return "; ".join([question.title for question in obj.question.all()])


admin.site.register(ElementQuestion, ElementQuestionAdmin)
admin.site.register(BaseQuestion, BaseQuestionAdmin)
admin.site.register(TextAnswer, TextAnswerAdmin)
admin.site.register(ChoiceAnswer, ChoiceAnswerAdmin)
admin.site.register(Task, TaskAdmin)
