from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.models import BaseBackgroundColor, TextBackgroundColor, TextTitleFont
from django.urls import reverse


def get_name_photo_file(instance, filename):
    return "/".join(['photos', str(instance.user_id), filename])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_birth = models.DateField(null=True, blank=True, verbose_name="Дата Рождения")
    photo = models.ImageField(upload_to=get_name_photo_file, null=True, blank=True, verbose_name="Фото")
    quote = models.CharField(max_length=100, null=True, blank=True, verbose_name="Цитата")

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"

    def get_absolute_url(self):
        return reverse('detail_profiles', kwargs={'user_id': self.user.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Point(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    number_points = models.PositiveIntegerField(blank=True, default=0, verbose_name="Количество очков")

    class Meta:
        verbose_name = "Баланс"
        verbose_name_plural = "Баланс"


@receiver(post_save, sender=User)
def create_user_point(sender, instance, created, **kwargs):
    if created:
        Point.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_point(sender, instance, **kwargs):
    instance.point.save()


class Visual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    base_background_color = models.ForeignKey(BaseBackgroundColor, on_delete=models.PROTECT, null=True, blank=True,
                                              verbose_name="Цвет основного фона")
    text_background_color = models.ForeignKey(TextBackgroundColor, on_delete=models.PROTECT, null=True, blank=True,
                                              verbose_name="Цвет фона текста", related_name="text_background_color")
    text_title_font = models.ForeignKey(TextTitleFont, on_delete=models.PROTECT, null=True, blank=True,
                                        verbose_name="Шрифт никнейма")

    class Meta:
        verbose_name = "Отображение карточки пользователя"
        verbose_name_plural = "Отображения карточек пользователя"


@receiver(post_save, sender=User)
def create_user_visual(sender, instance, created, **kwargs):
    if created:
        Visual.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_visual(sender, instance, **kwargs):
    instance.visual.save()
