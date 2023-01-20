from django.views.generic import ListView, DetailView
from profiles.utils import DataMixin
from .models import Task


class QuizzesListView(DataMixin, ListView):
    model = Task
    template_name = "quizzes/all_tasks.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Все задания"
        return context | self.get_user_context()


class QuizzesDetailView(DataMixin, DetailView):
    model = Task
    template_name = "quizzes/detail_task.html"
    context_object_name = "task"
    slug_url_kwarg = "task_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["task"]
        return context | self.get_user_context()
