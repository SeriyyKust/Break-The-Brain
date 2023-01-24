menu = [
    {"title": "Моя страница", "url_name": "my_page"},
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


class PointManager:
    @staticmethod
    def plus_points(user, number_points):
        """
        Adds points to the User
        :param user:
        :param number_points:
        :return: number of points after add
        """
        user.point.number_points += number_points
        user.save()
        return user.point.number_points

    @staticmethod
    def check_enough_points(user, number_points):
        """
        Checks if the User has enough points
        :param user:
        :param number_points:
        :return: True or False
        """
        if number_points > user.point.number_points:
            return False
        else:
            user.point.number_points -= number_points
            return True

    @staticmethod
    def minus_points(user, number_points):
        """
        Takes away points from the User
        :param user:
        :param number_points:
        :return: number of points after take away
        """
        if number_points > user.point.number_points:
            raise ValueError(f"The User has less points than {number_points}")
        else:
            user.point.number_points -= number_points
            user.save()
            return user.point.number_points
