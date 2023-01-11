from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def get_name_photo_file(instance):
    return 'photos/' + str(instance.id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_birth = models.DateField(null=True, blank=True, verbose_name="Дата Рождения")
    photo = models.ImageField(upload_to=get_name_photo_file, null=True, blank=True, verbose_name="Фото")
    quote = models.CharField(max_length=100, null=True, blank=True, verbose_name="Цитата")

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Point(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    number_points = models.PositiveIntegerField(blank=True, default=0)

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
