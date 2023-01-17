# Generated by Django 4.1.5 on 2023-01-17 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementquestion',
            name='category',
            field=models.CharField(choices=[('QUESTION', 'question'), ('ANSWER', 'answer')], default='Question', max_length=8, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='elementquestion',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='quizzes/elements/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='quizzes/tasks/%Y/%m/%d', verbose_name='Фото задания')),
                ('complexity', models.CharField(choices=[('EASY', 'easy'), ('MEDIUM', 'medium'), ('HARD', 'hard'), ('HARDCORE', 'hardcore')], default='easy', max_length=8, verbose_name='Сложность')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='URL')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('question', models.ManyToManyField(to='quizzes.basequestion', verbose_name='Вопросы задания')),
            ],
            options={
                'verbose_name': 'Задания',
            },
        ),
    ]
