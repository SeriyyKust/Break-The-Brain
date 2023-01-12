menu = [
    {"title": "Пользователи", "url_name": "all_profiles"},
    {"title": "Регистрация", "url_name": "registration_profiles"},
    {"title": "Войти", "url_name": "login_profiles"},
    {"title": "Выйти", "url_name": "logout_profiles"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        return context
