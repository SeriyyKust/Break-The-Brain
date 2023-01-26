from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import RegistrationUserForm, RegistrationProfileForm, LoginUserForm
from .utils import DataMixin, get_http_error_string, get_or_none


class ProfilesListView(DataMixin, ListView):
    model = User
    template_name = "profiles/all_profiles.html"
    context_object_name = "users"
    login_url = reverse_lazy("login_profiles")

    def get_queryset(self):
        return User.objects.all().select_related('profile', 'point')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Все пользователи"
        return context | self.get_user_context()


class ProfilesDetailView(LoginRequiredMixin, DataMixin, DetailView):
    model = User
    template_name = "profiles/detail_profiles.html"
    pk_url_kwarg = "user_id"
    context_object_name = "user"
    login_url = reverse_lazy("login_profiles")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["user"]
        return context | self.get_user_context()


class ProfilesMyPage(LoginRequiredMixin, DataMixin, ListView):
    model = User
    template_name = "profiles/my_page_profiles.html"
    context_object_name = "user"

    def get_queryset(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = context["user"]
        return context | self.get_user_context()


class RegistrationProfilesView(DataMixin, View):
    def get(self, request):
        user_form = RegistrationUserForm()
        profile_form = RegistrationProfileForm()
        context = {
            "title": "Регистрация",
            "user_form": user_form,
            "profile_form": profile_form,
        }
        context.update(self.get_user_context())
        return render(request, "profiles/registration_profiles.html", context)

    def post(self, request):
        user_form = RegistrationUserForm(request.POST)
        profile_form = RegistrationProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            user = get_or_none(User, username=user_form.cleaned_data['username'])
            if user is None:
                return HttpResponse(get_http_error_string(f"Add Profile Info: There isn't User with username "
                                                          f"'{user_form.cleaned_data['username']}'"))
            profile_form = RegistrationProfileForm(request.POST, instance=user.profile)
            profile_form.save()
            return redirect("login_profiles")
        context = {
            "title": "Регистрация",
            "user_form": user_form,
            "profile_form": profile_form,
        }
        context.update(self.get_user_context())
        return render(request, "profiles/registration_profiles.html", context)


class LoginProfilesView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "profiles/login_profiles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context | self.get_user_context()

    def get_success_url(self):
        return reverse_lazy("all_profiles")


def logout_profiles(request):
    print(request.user)
    logout(request)
    return redirect("login_profiles")