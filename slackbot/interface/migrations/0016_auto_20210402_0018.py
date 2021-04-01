# Generated by Django 3.1.7 on 2021-04-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0015_taskconfig_mode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskconfig',
            options={'verbose_name': 'Параметры задачи', 'verbose_name_plural': 'Параметры задачи'},
        ),
        migrations.AddField(
            model_name='taskconfig',
            name='day',
            field=models.IntegerField(default=5, help_text='В какой день недели отправить сообщение:', verbose_name='день'),
        ),
        migrations.AddField(
            model_name='taskconfig',
            name='hour',
            field=models.IntegerField(default=5, help_text='В который час отправить сообщение:', verbose_name='час'),
        ),
        migrations.AddField(
            model_name='taskconfig',
            name='minute',
            field=models.IntegerField(default=5, help_text='Во сколько минут отправить сообщение:', verbose_name='минута'),
        ),
        migrations.AlterField(
            model_name='taskconfig',
            name='mode',
            field=models.CharField(choices=[('mode1', 'Отправить сообщение сразу, если есть новый контент'), ('mode2', 'Отправить сообщение один раз в час, если есть новый контент'), ('mode3', 'Отправить сообщение один раз в день, если есть новый контент'), ('mode4', 'Отправить сообщение один раз в неделю, если есть новый контент')], default='mode1', max_length=5, verbose_name='задача'),
        ),
    ]