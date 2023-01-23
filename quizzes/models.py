from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from random import shuffle


ANSWER_TEXT_CATEGORY = "text"
ANSWER_PHOTO_CATEGORY = "photo"
ANSWER_CATEGORIES = ((ANSWER_TEXT_CATEGORY, ANSWER_TEXT_CATEGORY), (ANSWER_PHOTO_CATEGORY, ANSWER_PHOTO_CATEGORY))
TEXT_ANSWER_TEXT_MAX_LENGTH = 512
PHOTO_ANSWER_TITLE_MAX_LENGTH = 32


BASE_ELEMENT_QUESTION_TEXT_CATEGORY = "text"
BASE_ELEMENT_QUESTION_PHOTO_CATEGORY = "photo"
BASE_ELEMENT_QUESTION_CATEGORIES = ((BASE_ELEMENT_QUESTION_TEXT_CATEGORY, BASE_ELEMENT_QUESTION_TEXT_CATEGORY),
                                    (BASE_ELEMENT_QUESTION_PHOTO_CATEGORY, BASE_ELEMENT_QUESTION_PHOTO_CATEGORY))
BASE_ELEMENT_QUESTION_TEXT_MAX_LENGTH = 1024
PHOTO_ELEMENT_QUESTION_TITLE_MAX_LENGTH = 32


BASE_QUESTION_TEXT_CATEGORY = "text"
BASE_QUESTION_CHOICE_CATEGORY = "choice"
BASE_QUESTION_SLUG_MAX_LENGTH = 64
BASE_QUESTION_CATEGORIES = ((BASE_QUESTION_TEXT_CATEGORY, BASE_QUESTION_TEXT_CATEGORY),
                            (BASE_QUESTION_CHOICE_CATEGORY, BASE_QUESTION_CHOICE_CATEGORY))


TASK_EASY_CATEGORY = "easy"
TASK_MEDIUM_CATEGORY = "medium"
TASK_HARD_CATEGORY = "hard"
TASK_HARDCORE_CATEGORY = "hardcore"
TASK_CATEGORIES = ((TASK_EASY_CATEGORY, TASK_EASY_CATEGORY), (TASK_MEDIUM_CATEGORY, TASK_MEDIUM_CATEGORY),
                   (TASK_HARD_CATEGORY, TASK_HARD_CATEGORY), (TASK_HARDCORE_CATEGORY, TASK_HARDCORE_CATEGORY))
TASK_TITLE_MAX_LENGTH = 64


class Answer(models.Model):
    category = models.CharField(max_length=max(len(category[0]) for category in ANSWER_CATEGORIES),
                                choices=ANSWER_CATEGORIES,
                                default=ANSWER_TEXT_CATEGORY,
                                verbose_name="Категория ответа")

    class Meta:
        verbose_name = "Все ответы"
        verbose_name_plural = "Все ответы"
    
    def __str__(self):
        try:
            if self.category == ANSWER_TEXT_CATEGORY:
                return TextAnswer.objects.get(pk=self.pk).text[:16]
            else:
                return PhotoAnswer.objects.get(pk=self.pk).title[:16]
        except TextAnswer.DoesNotExist:
            return PhotoAnswer.objects.get(pk=self.pk).title[:16]
        except PhotoAnswer.DoesNotExist:
            return TextAnswer.objects.get(pk=self.pk).text[:16]


class TextAnswer(Answer):
    text = models.CharField(max_length=TEXT_ANSWER_TEXT_MAX_LENGTH, unique=True, verbose_name="Текст ответа")

    class Meta:
        verbose_name = "Текстовый ответ"
        verbose_name_plural = "Текстовые ответы"

    def __str__(self):
        return self.text[:16]


class PhotoAnswer(Answer):
    title = models.CharField(max_length=PHOTO_ANSWER_TITLE_MAX_LENGTH, unique=True, verbose_name="Заголовок фото")
    photo = models.ImageField(upload_to="quizzes/answers/%Y/%m/%d", verbose_name="Фото ответа")

    class Meta:
        verbose_name = "Фото ответ"
        verbose_name_plural = "Фото ответы"

    def __str__(self):
        return self.title[:16]


class BaseElementQuestion(models.Model):
    text = models.CharField(max_length=BASE_ELEMENT_QUESTION_TEXT_MAX_LENGTH, verbose_name="Текст вопроса")
    category = models.CharField(max_length=max(len(category[0]) for category in BASE_ELEMENT_QUESTION_CATEGORIES),
                                choices=BASE_ELEMENT_QUESTION_CATEGORIES,
                                default=BASE_ELEMENT_QUESTION_TEXT_CATEGORY,
                                verbose_name="Категория вопроса")

    class Meta:
        verbose_name = "Стандартный элемент вопроса"
        verbose_name_plural = "Стандартные элементы вопроса"

    def __str__(self):
        return self.text[:16]


class PhotoElementQuestion(BaseElementQuestion):
    title = models.CharField(max_length=PHOTO_ELEMENT_QUESTION_TITLE_MAX_LENGTH, unique=True,
                             verbose_name="Заголовок фото")
    photo = models.ImageField(upload_to="quizzes/questions/%Y/%m/%d", verbose_name="Фото вопроса")

    class Meta:
        verbose_name = "Фото элемент вопроса"
        verbose_name_plural = "Фото элементы вопроса"

    def __str__(self):
        return self.title[:16]


class BaseQuestion(models.Model):
    question = models.ForeignKey(BaseElementQuestion, on_delete=models.PROTECT, verbose_name="Вопрос")
    correct_answer = models.ForeignKey(Answer, on_delete=models.PROTECT, verbose_name="Правильный ответ")
    date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    cost = models.PositiveIntegerField(default=0, verbose_name="Цена")
    category = models.CharField(max_length=max(len(element[0]) for element in BASE_QUESTION_CATEGORIES),
                                choices=BASE_QUESTION_CATEGORIES,
                                default=BASE_QUESTION_TEXT_CATEGORY,
                                verbose_name="Тип вопроса")
    slug = models.SlugField(max_length=BASE_QUESTION_SLUG_MAX_LENGTH, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Стандартный Вопрос"
        verbose_name_plural = "Стандартные Вопросы"

    def __str__(self):
        return self.question.text[:16]

    def check_answer(self, cleaned_data):
        if self.correct_answer.category == ANSWER_TEXT_CATEGORY:
            correct_answer = TextAnswer.objects.get(pk=self.correct_answer.pk).text
        elif self.correct_answer.category == ANSWER_PHOTO_CATEGORY:
            correct_answer = PhotoAnswer.objects.get(pk=self.correct_answer.pk)
        else:
            raise TypeError
        if correct_answer == cleaned_data[self.question.text]:
            return True
        else:
            return False


class ChoiceQuestion(BaseQuestion):
    wrong_answer_1 = models.ForeignKey(Answer, on_delete=models.PROTECT, verbose_name="Неверный ответ 1",
                                       related_name="wrong_answer_1")
    wrong_answer_2 = models.ForeignKey(Answer, on_delete=models.PROTECT, verbose_name="Неверный ответ 2",
                                       related_name="wrong_answer_2")
    wrong_answer_3 = models.ForeignKey(Answer, on_delete=models.PROTECT, verbose_name="Неверный ответ 3",
                                       related_name="wrong_answer_3")

    class Meta:
        verbose_name = "Выборочный вопрос"
        verbose_name_plural = "Выборочные вопросы"

    def get_shuffle_answer_list(self):
        return_list = [super(ChoiceQuestion, self).correct_answer, self.wrong_answer_1, self.wrong_answer_2,
                       self.wrong_answer_3]
        shuffle(return_list)
        return return_list


class Task(models.Model):
    title = models.CharField(max_length=TASK_TITLE_MAX_LENGTH, unique=True, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="quizzes/tasks/%Y/%m/%d", null=True, blank=True, verbose_name="Фото задания")
    complexity = models.CharField(max_length=max(len(element[0]) for element in TASK_CATEGORIES ),
                                  choices=TASK_CATEGORIES,
                                  default=TASK_EASY_CATEGORY,
                                  verbose_name="Сложность")
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Владелец")
    questions = models.ManyToManyField(BaseQuestion, verbose_name="Вопросы задания")
    slug = models.SlugField(max_length=64, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_quizzes', kwargs={'task_slug': self.slug})

    @property
    def points(self):
        return sum(question.cost for question in self.questions.all())
