# Generated by Django 3.1.7 on 2021-03-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackbots',
            name='agent',
            field=models.CharField(max_length=255, null=True, verbose_name='выдаваемый агент'),
        ),
    ]
