# Generated by Django 4.1.5 on 2023-01-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseBackgroundColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('profiles-background-color__white', 'profiles-background-color__white'), ('profiles-background-color__purple', 'profiles-background-color__purple'), ('profiles-background-color__scarlet', 'profiles-background-color__scarlet'), ('profiles-background-color__white_grey', 'profiles-background-color__white_grey'), ('profiles-background-color__black_grey', 'profiles-background-color__black_grey'), ('profiles-background-color__height_grey', 'profiles-background-color__height_grey')], db_index=True, default='profiles-background-color__white', max_length=38, unique=True, verbose_name='Название стиля')),
                ('price', models.PositiveIntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'Цвет основного фона',
                'verbose_name_plural': 'Цвета основного фона',
            },
        ),
        migrations.CreateModel(
            name='TextBackgroundColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('profiles-background-color__white', 'profiles-background-color__white'), ('profiles-background-color__purple', 'profiles-background-color__purple'), ('profiles-background-color__scarlet', 'profiles-background-color__scarlet'), ('profiles-background-color__white_grey', 'profiles-background-color__white_grey'), ('profiles-background-color__black_grey', 'profiles-background-color__black_grey'), ('profiles-background-color__height_grey', 'profiles-background-color__height_grey')], db_index=True, default='profiles-background-color__white', max_length=38, unique=True, verbose_name='Название стиля')),
                ('price', models.PositiveIntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'Цвет фона текста',
                'verbose_name_plural': 'Цвета фона текста',
            },
        ),
        migrations.CreateModel(
            name='TextTitleFont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('profiles-title__times', 'profiles-title__times'), ('profiles-title__arial', 'profiles-title__arial'), ('profiles-title__fantasy', 'profiles-title__fantasy'), ('profiles-title__monospace', 'profiles-title__monospace'), ('profiles-title__cursive', 'profiles-title__cursive')], db_index=True, default='profiles-title__times', max_length=25, unique=True, verbose_name='Название шрифта')),
                ('price', models.PositiveIntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'Шрифт никнейма',
                'verbose_name_plural': 'Шрифты никнеймов',
            },
        ),
    ]
