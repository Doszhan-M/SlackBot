from django.db import models


class Posts(models.Model):
    headline = models.CharField(max_length=255, null=False,
                                verbose_name='Заголовок')
    public_time = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата захвата')
    link = models.URLField(max_length=1000, verbose_name='Ссылка поста')
    status = models.CharField(max_length=255, default='waiting', null=False,
                              verbose_name='Статус')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class SlackBots(models.Model):
    name = models.CharField(max_length=255, null=False,
                             verbose_name='Название бота',)
    token = models.CharField(max_length=255, null=False,
                             verbose_name='Токен',)
    channel = models.CharField(max_length=255, default='#general',
                               verbose_name='канал бота', help_text='внимание, бот должен быть авторизован на данном канале',)
    work1 = 'work1'
    work2 = 'work2'
    WORK = [(work1, 'Задача №1'), (work2, 'Задача №2')]
    task = models.CharField(max_length=5, choices=WORK,
                            default=work1, verbose_name='задача')
    delay = models.IntegerField(default=3, verbose_name='задержка для бота',
                                help_text='задержка между отправками сообщении',)
    editor_text = models.TextField(
        default=f"Всем привет! На нашем хабре появились новые статьи.\n Не забудьте посмотреть:\n\n")

    class Meta:
        verbose_name = 'SlackBot'
        verbose_name_plural = 'SlackBots'


class TaskConfig(models.Model):
    name = models.CharField(default='task1', max_length=255,
                            null=False, help_text='для захвата модели',)
    task_id = models.CharField(
        max_length=255, null=False, help_text='для захвата модели',)
    parse_delay = models.IntegerField(default=5, verbose_name='задержка для парсинга',
                                      help_text='задержка в минутах между запросами на сайт',)
    mode1 = 'mode1'
    mode2 = 'mode2'
    mode3 = 'mode3'
    mode4 = 'mode4'
    MODE = [(mode1, 'Отправить сообщение сразу, если есть новый контент'),
            (mode2, 'Отправить сообщение один раз в час, если есть новый контент'),
            (mode3, 'Отправить сообщение один раз в день, если есть новый контент'),
            (mode4, 'Отправить сообщение один раз в неделю, если есть новый контент')]
    mode = models.CharField(max_length=5, choices=MODE,
                            default=mode1, verbose_name='задача')
    minute = models.IntegerField(default=5, verbose_name='минута',
                                      help_text='Во сколько минут отправить сообщение:',)
    hour = models.IntegerField(default=5, verbose_name='час',
                                      help_text='В который час отправить сообщение:',)
    day = models.IntegerField(default=5, verbose_name='день',
                                      help_text='В какой день недели отправить сообщение:',)


    class Meta:
        verbose_name = ("Параметры задачи")
        verbose_name_plural = ("Параметры задачи")
