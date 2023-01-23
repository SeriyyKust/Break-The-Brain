from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render, reverse, redirect
from profiles.utils import DataMixin
from .models import Task
from .utils import FormManagerTask

from .models import Task, PhotoElementQuestion
from .models import BASE_ELEMENT_QUESTION_PHOTO_CATEGORY, BASE_QUESTION_TEXT_CATEGORY, BASE_QUESTION_CHOICE_CATEGORY, \
    ANSWER_TEXT_CATEGORY, ANSWER_PHOTO_CATEGORY
from .forms import TextAnswerForm, ChoiceAnswerForm, ChoiceWithPhotoAnswerForm


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


class QuizzesPassingTask(DataMixin, View):
    def get(self, request, task_slug):
        task = Task.objects.get(slug=task_slug)
        context = {"title": task.title,
                   "questions_forms": FormManagerTask.get_forms_list(task=task),
                   "task_slug": task_slug}
        context.update(self.get_user_context())
        return render(request, 'quizzes/passing_task.html', context=context)

    def post(self, request, task_slug):
        task = Task.objects.get(slug=task_slug)
        count_point = FormManagerTask.check_forms_with_answers(task=task, answer_dict=request.POST)
        print(count_point)
        return redirect(reverse('all_quizzes'))
