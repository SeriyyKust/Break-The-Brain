from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render, reverse, redirect
from profiles.utils import DataMixin, get_or_none, get_http_error_string
from .models import Task
from .utils import FormManagerTask
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse


class QuizzesListView(DataMixin, ListView):
    model = Task
    template_name = "quizzes/all_tasks.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Все задания"
        return context | self.get_user_context()


class QuizzesDetailView(LoginRequiredMixin, DataMixin, DetailView):
    model = Task
    template_name = "quizzes/detail_task.html"
    context_object_name = "task"
    slug_url_kwarg = "task_slug"
    login_url = reverse_lazy("login_profiles")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["task"]
        return context | self.get_user_context()


class QuizzesPassingTask(LoginRequiredMixin, DataMixin, View):
    login_url = reverse_lazy("login_profiles")

    def get(self, request, task_slug):
        task = get_or_none(Task, slug=task_slug)
        if task is None:
            return HttpResponse(get_http_error_string(f"Create Form: There isn't task with slug '{task_slug}'"))
        context = {"title": task.title,
                   "questions_forms": FormManagerTask.get_forms_list(task=task),
                   "task_slug": task_slug}
        context.update(self.get_user_context())
        return render(request, 'quizzes/passing_task.html', context=context)

    def post(self, request, task_slug):
        task = get_or_none(Task, slug=task_slug)
        if task is None:
            return HttpResponse(get_http_error_string(f"Check Form: There isn't task with slug '{task_slug}'"))
        count_point = FormManagerTask.check_forms_with_answers(task=task, answer_dict=request.POST)
        print(count_point)
        return redirect(reverse('all_quizzes'))
