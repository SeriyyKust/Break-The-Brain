# Generated by Django 4.1.5 on 2023-01-26 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('text', 'text'), ('photo', 'photo')], default='text', max_length=5, verbose_name='Категория ответа')),
            ],
            options={
                'verbose_name': 'Все ответы',
                'verbose_name_plural': 'Все ответы',
            },
        ),
        migrations.CreateModel(
            name='BaseElementQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024, verbose_name='Текст вопроса')),
                ('category', models.CharField(choices=[('text', 'text'), ('photo', 'photo')], default='text', max_length=5, verbose_name='Категория вопроса')),
            ],
            options={
                'verbose_name': 'Стандартный элемент вопроса',
                'verbose_name_plural': 'Стандартные элементы вопроса',
            },
        ),
        migrations.CreateModel(
            name='BaseQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('category', models.CharField(choices=[('text', 'text'), ('choice', 'choice')], default='text', max_length=6, verbose_name='Тип вопроса')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='URL')),
                ('correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quizzes.answer', verbose_name='Правильный ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quizzes.baseelementquestion', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Стандартный Вопрос',
                'verbose_name_plural': 'Стандартные Вопросы',
            },
        ),
        migrations.CreateModel(
            name='PhotoAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quizzes.answer')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='Заголовок фото')),
                ('photo', models.ImageField(upload_to='quizzes/answers/%Y/%m/%d', verbose_name='Фото ответа')),
            ],
            options={
                'verbose_name': 'Фото ответ',
                'verbose_name_plural': 'Фото ответы',
            },
            bases=('quizzes.answer',),
        ),
        migrations.CreateModel(
            name='PhotoElementQuestion',
            fields=[
                ('baseelementquestion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quizzes.baseelementquestion')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='Заголовок фото')),
                ('photo', models.ImageField(upload_to='quizzes/questions/%Y/%m/%d', verbose_name='Фото вопроса')),
            ],
            options={
                'verbose_name': 'Фото элемент вопроса',
                'verbose_name_plural': 'Фото элементы вопроса',
            },
            bases=('quizzes.baseelementquestion',),
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quizzes.answer')),
                ('text', models.CharField(max_length=512, unique=True, verbose_name='Текст ответа')),
            ],
            options={
                'verbose_name': 'Текстовый ответ',
                'verbose_name_plural': 'Текстовые ответы',
            },
            bases=('quizzes.answer',),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Заголовок')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='quizzes/tasks/%Y/%m/%d', verbose_name='Фото задания')),
                ('complexity', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard'), ('hardcore', 'hardcore')], default='easy', max_length=8, verbose_name='Сложность')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='URL')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('questions', models.ManyToManyField(to='quizzes.basequestion', verbose_name='Вопросы задания')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('basequestion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quizzes.basequestion')),
                ('wrong_answer_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wrong_answer_1', to='quizzes.answer', verbose_name='Неверный ответ 1')),
                ('wrong_answer_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wrong_answer_2', to='quizzes.answer', verbose_name='Неверный ответ 2')),
                ('wrong_answer_3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wrong_answer_3', to='quizzes.answer', verbose_name='Неверный ответ 3')),
            ],
            options={
                'verbose_name': 'Выборочный вопрос',
                'verbose_name_plural': 'Выборочные вопросы',
            },
            bases=('quizzes.basequestion',),
        ),
    ]
