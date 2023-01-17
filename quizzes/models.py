from django.db import models
from django.contrib.auth.models import User


CATEGORY_ELEMENT_QUESTION_CHOICES = (("QUESTION", "question"), ("ANSWER", "answer"))
CATEGORY_COMPLEXITY_CHOICES = (("EASY", "easy"), ("MEDIUM", "medium"), ("HARD", "hard"), ("HARDCORE", "hardcore"))
MAX_LENGTH_QUESTION = 1024
MAX_LENGTH_CORRECT_ANSWER = 512


class ElementQuestion(models.Model):
    title = models.CharField(max_length=MAX_LENGTH_QUESTION, unique=True, verbose_name="Текст")
    photo = models.ImageField(upload_to="quizzes/elements/%Y/%m/%d", null=True, blank=True, verbose_name="Фото")
    category = models.CharField(max_length=max(len(element[0]) for element in CATEGORY_ELEMENT_QUESTION_CHOICES),
                                choices=CATEGORY_ELEMENT_QUESTION_CHOICES, default="Question",
                                verbose_name="Категория")

    class Meta:
        verbose_name = "Элемент вопроса"
        verbose_name_plural = "Элементы вопросов"

    def __str__(self):
        return self.title


class BaseQuestion(models.Model):
    title = models.CharField(max_length=64, unique=True, db_index=True, verbose_name="Заголовок")
    question = models.ForeignKey(ElementQuestion, on_delete=models.PROTECT, verbose_name="Вопрос")
    date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    cost = models.PositiveIntegerField(default=0, verbose_name="Цена")
    slug = models.SlugField(max_length=MAX_LENGTH_QUESTION, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title


class TextAnswer(BaseQuestion):
    correct_answer = models.CharField(max_length=MAX_LENGTH_CORRECT_ANSWER, verbose_name="Верный ответ")

    class Meta:
        verbose_name = "Текстовый вопрос"
        verbose_name_plural = "Текстовые вопросы"

    def __str__(self):
        return self.correct_answer[:10]


class ChoiceAnswer(BaseQuestion):
    correct_answer = models.ForeignKey(ElementQuestion, on_delete=models.PROTECT, verbose_name="Верный ответ",
                                       related_name="correct_answer")
    wrong_answer_1 = models.ForeignKey(ElementQuestion, on_delete=models.PROTECT, verbose_name="Неверный ответ 1",
                                       related_name="wrong_answer_1")
    wrong_answer_2 = models.ForeignKey(ElementQuestion, on_delete=models.PROTECT, verbose_name="Неверный ответ 2",
                                       related_name="wrong_answer_2")
    wrong_answer_3 = models.ForeignKey(ElementQuestion, on_delete=models.PROTECT, verbose_name="Неверный ответ 3",
                                       related_name="wrong_answer_3")

    class Meta:
        verbose_name = "Выборочный вопрос"
        verbose_name_plural = "Выборочные вопросы"

    def __str__(self):
        return self.correct_answer.title[:10]


class Task(models.Model):
    title = models.CharField(max_length=64, unique=True, db_index=True, verbose_name="Название")
    photo = models.ImageField(upload_to="quizzes/tasks/%Y/%m/%d",null=True, blank=True, verbose_name="Фото задания")
    complexity = models.CharField(max_length=max(len(element[0]) for element in CATEGORY_COMPLEXITY_CHOICES),
                                  choices=CATEGORY_COMPLEXITY_CHOICES, default="easy", verbose_name="Сложность")
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Владелец")
    question = models.ManyToManyField(BaseQuestion, verbose_name="Вопросы задания")
    slug = models.SlugField(max_length=64, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.title
