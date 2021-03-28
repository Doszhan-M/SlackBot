from django.db import models


class Posts(models.Model):
    headline = models.CharField(max_length=255, null=False,
                                verbose_name='Заголовок')
    public_time = models.DateTimeField(verbose_name='Дата публикации')
    link = models.URLField(max_length=1000, verbose_name='Ссылка поста')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class SlackBots(models.Model):
    flag = models.CharField(max_length=255, null=False,
                             verbose_name='стратегия бота',)
    token = models.CharField(max_length=255, null=False,
                             verbose_name='Токен',)
    url = models.URLField(
        max_length=1000, verbose_name='Ссылка страницы парсинга')
    agent = models.TextField(
        default="'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36'", 
        verbose_name='выдаваемый агент',)
    host = models.URLField(max_length=1000, default='https://m.habr.com', verbose_name='Ссылка страницы парсинга',
                           help_text='хост нужно передать без слэша в конце',)
    channel = models.CharField(max_length=255, default='#general',
                             verbose_name='канал бота', help_text='внимание, бот должен быть авторизован в данном канале',)

    work1 = 'work1'
    work2 = 'work2'
    WORK = [(work1, 'Задача №1'), (work2, 'Задача №2')]
    flag = models.CharField(max_length=5, choices=WORK, default=work1)
    

    class Meta:
        verbose_name = 'SlackBot'
        verbose_name_plural = 'SlackBots'
