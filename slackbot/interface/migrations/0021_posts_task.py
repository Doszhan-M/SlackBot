# Generated by Django 3.1.7 on 2021-04-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0020_auto_20210402_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='task',
            field=models.CharField(default=1, help_text='принадлежность к задаче', max_length=255),
            preserve_default=False,
        ),
    ]
