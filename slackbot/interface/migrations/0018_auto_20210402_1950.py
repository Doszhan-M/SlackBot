# Generated by Django 3.1.7 on 2021-04-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0017_slackbots_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.TextField(default=1, verbose_name='Теги'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slackbots',
            name='delay',
            field=models.IntegerField(default=3, help_text='нужно выбрать', verbose_name='Номер задачи'),
        ),
    ]
