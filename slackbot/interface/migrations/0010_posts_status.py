# Generated by Django 3.1.7 on 2021-03-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0009_auto_20210328_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='status',
            field=models.CharField(default='waiting', max_length=255, verbose_name='Статус'),
        ),
    ]
