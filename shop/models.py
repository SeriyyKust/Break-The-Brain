from django.db import models
from django.urls import reverse


COLOR_WHITE = "profiles-background-color__white"
COLOR_PURPLE = "profiles-background-color__purple"
COLOR_SCARLET = "profiles-background-color__scarlet"
COLOR_WHITE_GREY = "profiles-background-color__white_grey"
COLOR_BLACK_GREY = "profiles-background-color__black_grey"
COLOR_HEIGHT_GREY = "profiles-background-color__height_grey"

FONT_TIMES = "profiles-title__times"
FONT_ARIAL = "profiles-title__arial"
FONT_FANTASY = "profiles-title__fantasy"
FONT_MONOSPACE = "profiles-title__monospace"
FONT_CURSIVE = "profiles-title__cursive"

COLOR_CHOICES = (
    (COLOR_WHITE, COLOR_WHITE),
    (COLOR_PURPLE, COLOR_PURPLE),
    (COLOR_SCARLET, COLOR_SCARLET),
    (COLOR_WHITE_GREY, COLOR_WHITE_GREY),
    (COLOR_BLACK_GREY, COLOR_BLACK_GREY),
    (COLOR_HEIGHT_GREY, COLOR_HEIGHT_GREY),
)

FONT_CHOICES = (
    (FONT_TIMES, FONT_TIMES),
    (FONT_ARIAL, FONT_ARIAL),
    (FONT_FANTASY, FONT_FANTASY),
    (FONT_MONOSPACE, FONT_MONOSPACE),
    (FONT_CURSIVE, FONT_CURSIVE),
)


class BaseBackgroundColor(models.Model):
    title = models.CharField(unique=True,
                             db_index=True,
                             max_length=max(len(color[0]) for color in COLOR_CHOICES),
                             choices=COLOR_CHOICES,
                             default=COLOR_WHITE,
                             verbose_name="Название стиля")
    price = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Цвет основного фона"
        verbose_name_plural = "Цвета основного фона"

    def __str__(self):
        return " ".join(self.title.split('__')[1].split('_'))

    def full_str(self):
        return self.title

    @staticmethod
    def get_verbose_name():
        return "Цвет основного фона"

    @staticmethod
    def get_absolute_url():
        return reverse("base_background_color_shop")

    @staticmethod
    def get_type():
        return BaseBackgroundColor


class TextBackgroundColor(models.Model):
    title = models.CharField(unique=True,
                             db_index=True,
                             max_length=max(len(color[0]) for color in COLOR_CHOICES),
                             choices=COLOR_CHOICES,
                             default=COLOR_WHITE,
                             verbose_name="Название стиля")
    price = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Цвет фона текста"
        verbose_name_plural = "Цвета фона текста"

    def __str__(self):
        return " ".join(self.title.split('__')[1].split('_'))

    def full_str(self):
        return self.title

    @staticmethod
    def get_verbose_name():
        return "Цвет фона текста"

    @staticmethod
    def get_absolute_url():
        return reverse("text_background_color_shop")

    @staticmethod
    def get_type():
        return TextBackgroundColor


class TextTitleFont(models.Model):
    title = models.CharField(unique=True,
                             db_index=True,
                             max_length=max(len(font[0]) for font in FONT_CHOICES),
                             choices=FONT_CHOICES,
                             default=FONT_TIMES,
                             verbose_name="Название шрифта")
    price = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Шрифт никнейма"
        verbose_name_plural = "Шрифты никнеймов"

    def __str__(self):
        return " ".join(self.title.split('__')[1].split('_'))

    def full_str(self):
        return self.title

    @staticmethod
    def get_verbose_name():
        return "Шрифт никнейма"

    @staticmethod
    def get_absolute_url():
        return reverse("text_title_font_shop")

    @staticmethod
    def get_type():
        return TextTitleFont


SHOP_CATEGORIES = (BaseBackgroundColor, TextBackgroundColor, TextTitleFont)
BASE_BACKGROUND_COLOR_DEFAULT = COLOR_WHITE
TEXT_BACKGROUND_COLOR_DEFAULT = COLOR_WHITE
TEXT_TITLE_FONT_DEFAULT = FONT_TIMES
