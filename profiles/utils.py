menu = [
    {"title": "Моя страница", "url_name": "all_profiles"},
    {"title": "Пользователи", "url_name": "all_profiles"},
    {"title": "Тесты", "url_name": "all_quizzes"},
]

login = [
    {"title": "Регистрация", "url_name": "registration_profiles"},
    {"title": "Войти", "url_name": "login_profiles"},
    {"title": "Выйти", "url_name": "logout_profiles"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context_login = login.copy()
        context_menu = menu.copy()
        if self.request.user.is_authenticated:
            context_login.pop(0)
            context_login.pop(0)
        else:
            context_menu.pop(0)
            context_login.pop(2)
        context["login"] = context_login
        context["menu"] = context_menu
        return context


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def get_http_error_string(info):
    print(f"####################################################"
          f"\nError!!!\n{info}\n"
          f"####################################################")
    return f"<p><h1>Sorry.</h1></p><p><h1>There was a problem.</h1></p>"
