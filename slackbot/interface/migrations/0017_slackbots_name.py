# Generated by Django 3.1.7 on 2021-04-02 03:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0016_auto_20210402_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='slackbots',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Название бота'),
            preserve_default=False,
        ),
    ]
