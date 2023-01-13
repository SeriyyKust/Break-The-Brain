menu = [
    {"title": "Моя страница", "url_name": "all_profiles"},
    {"title": "Пользователи", "url_name": "all_profiles"},
    {"title": "Тесты", "url_name": "all_profiles"},
]

login = [
    {"title": "Регистрация", "url_name": "registration_profiles"},
    {"title": "Войти", "url_name": "login_profiles"},
    {"title": "Выйти", "url_name": "logout_profiles"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        context["login"] = login
        return context
