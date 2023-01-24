from django.contrib import admin
from .models import Answer, TextAnswer, PhotoAnswer, BaseElementQuestion, PhotoElementQuestion, BaseQuestion, \
    ChoiceQuestion, Task


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "category", )
    list_display_links = ("id", )
    list_editable = ("category", )


class TextAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "text", )
    list_display_links = ("id",)
    list_editable = ("text", )


class PhotoAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", )
    list_display_links = ("id",)


class BaseElementQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "category")
    list_display_links = ("id",)
    list_editable = ("text", "category")


class PhotoElementQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", )
    list_display_links = ("id",)


class BaseQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "correct_answer", "cost", "category", "slug")
    list_editable = ("question", "correct_answer", "cost", "category", "slug")
    list_display_links = ("id", )
    search_fields = ("id", )


class ChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "wrong_answer_1", "wrong_answer_2", "wrong_answer_3")
    list_display_links = ("id",)
    list_editable = ("wrong_answer_1", "wrong_answer_2", "wrong_answer_3")


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "photo", "complexity", "owner", "questions_task", "date", "slug")
    list_display_links = ("title", )
    search_fields = ("title", )
    list_editable = ("photo", "complexity", "owner", "slug")

    def questions_task(self, obj):
        return " ||\n".join([question.question.text for question in obj.questions.all()])


admin.site.register(Answer, AnswerAdmin)
admin.site.register(TextAnswer, TextAnswerAdmin)
admin.site.register(PhotoAnswer, PhotoAnswerAdmin)
admin.site.register(BaseElementQuestion, BaseElementQuestionAdmin)
admin.site.register(PhotoElementQuestion, PhotoElementQuestionAdmin)
admin.site.register(BaseQuestion, BaseQuestionAdmin)
admin.site.register(ChoiceQuestion, ChoiceQuestionAdmin)
admin.site.register(Task, TaskAdmin)
