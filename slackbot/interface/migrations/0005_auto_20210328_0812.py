# Generated by Django 3.1.7 on 2021-03-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_auto_20210328_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackbots',
            name='agent',
            field=models.TextField(default='afafa', verbose_name='выдаваемый агент'),
        ),
    ]