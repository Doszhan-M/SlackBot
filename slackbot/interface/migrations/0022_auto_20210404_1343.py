# Generated by Django 3.1.7 on 2021-04-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0021_posts_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskconfig',
            options={'verbose_name': 'Параметры задачи', 'verbose_name_plural': 'Параметры задач'},
        ),
        migrations.AlterField(
            model_name='slackbots',
            name='bot_tags',
            field=models.CharField(help_text='Для задачи №2 введите теги через запятую', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='taskconfig',
            name='task',
            field=models.CharField(choices=[('task1', 'Задача №1'), ('task2', 'Задача №2')], max_length=5, verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='taskconfig',
            name='task_id',
            field=models.CharField(help_text='Для управления задачей', max_length=255),
        ),
    ]
