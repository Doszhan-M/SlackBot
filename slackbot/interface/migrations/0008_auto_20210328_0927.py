# Generated by Django 3.1.7 on 2021-03-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0007_auto_20210328_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackbots',
            name='flag',
            field=models.CharField(choices=[('work1', 'Задача №1'), ('work2', 'Задача №2')], default='work1', max_length=5),
        ),
    ]