from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


class ProfilesListView(ListView):
    model = User
    template_name = "profiles/all_profiles.html"
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.all().select_related('profile', 'point')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Все пользователи"
        return context


class ProfilesDetailView(DetailView):
    model = User
    template_name = "profiles/detail_profiles.html"
    pk_url_kwarg = "user_id"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = context["user"]
        return context
