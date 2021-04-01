# Generated by Django 3.1.7 on 2021-03-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('public_time', models.DateTimeField(verbose_name='Дата публикации')),
                ('link', models.URLField(max_length=1000, verbose_name='Ссылка поста')),
            ],
        ),
        migrations.CreateModel(
            name='SlackBots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, verbose_name='Токен')),
                ('url', models.URLField(max_length=1000, verbose_name='Ссылка страницы парсинга')),
                ('agent', models.CharField(max_length=255, verbose_name='выдаваемый агент')),
                ('host', models.URLField(default='https://m.habr.com', help_text='хост нужно передать без слэша в конце', max_length=1000, verbose_name='Ссылка страницы парсинга')),
            ],
        ),
    ]