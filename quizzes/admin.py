from django.contrib import admin
from .models import Answer, TextAnswer, PhotoAnswer, BaseElementQuestion, PhotoElementQuestion, BaseQuestion, \
    ChoiceQuestion, Task


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "category", )
    list_display_links = ("id", )
    list_editable = ("category", )


@admin.register(TextAnswer)
class TextAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "text", )
    list_display_links = ("id",)
    list_editable = ("text", )


@admin.register(PhotoAnswer)
class PhotoAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", )
    list_display_links = ("id",)


@admin.register(BaseElementQuestion)
class BaseElementQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "category")
    list_display_links = ("id",)
    list_editable = ("text", "category")


@admin.register(PhotoElementQuestion)
class PhotoElementQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", )
    list_display_links = ("id",)


@admin.register(BaseQuestion)
class BaseQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "correct_answer", "cost", "category")
    list_editable = ("question", "correct_answer", "cost", "category")
    list_display_links = ("id", )
    search_fields = ("id", )


@admin.register(ChoiceQuestion)
class ChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "wrong_answer_1", "wrong_answer_2", "wrong_answer_3")
    list_display_links = ("id",)
    list_editable = ("wrong_answer_1", "wrong_answer_2", "wrong_answer_3")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "photo", "complexity", "owner", "questions_task", "date", "slug")
    list_display_links = ("title", )
    search_fields = ("title", )
    list_editable = ("photo", "complexity", "owner", "slug")
    prepopulated_fields = {"slug": ("title", )}

    def questions_task(self, obj):
        return " ||\n".join([question.question.text for question in obj.questions.all()])
