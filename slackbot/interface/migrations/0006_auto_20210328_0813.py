# Generated by Django 3.1.7 on 2021-03-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0005_auto_20210328_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackbots',
            name='agent',
            field=models.TextField(default="'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36'", verbose_name='выдаваемый агент'),
        ),
    ]
