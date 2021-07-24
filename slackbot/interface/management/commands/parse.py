from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from interface.models import Posts, SlackBots
from interface.management.commands.random_agent import get_agent
from django.utils import timezone
from slack import WebClient
import time
import random


class Command(BaseCommand):
    help = 'Оповещать сотрудников SF в Slack о выходе всех новых статей по всем тематикам в блоге компании на habr'

    def handle(self, *args, **options):

        # url страницы для парсинга
        URL = 'https://m.habr.com/ru/company/skillfactory/blog/'
        # выдаваемый агент для сайта
        HEADERS = {'User-Agent' : get_agent(),
        'Accept' : '*/*'}
        # хост нужно передать без слэша в конце
        HOST = 'https://habr.com'
        # Create a slack client
        SLACKBOT = WebClient(token='')


        def get_html(url, params=None):
            """получить html код всей страницы"""
            # на вход принимает URL, params для парсинга пагинации
            r = requests.get(url, headers = HEADERS, params=params)
            return r


        def get_content(html):
            """создаем python объекты из спарсенной страницы"""
            # работа библиотеки BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            # получаем все статьи вместе с временем публикации
            items = soup.find_all('div', class_ = 'tm-article-snippet')
            flag = False
            for item in items:  
                # Получить время поста
                public_time = item.find('span', class_ = 'tm-article-snippet__datetime-published').get_text(strip=True)
                # Получить заголовок поста
                headline=item.find('h2', class_ = 'tm-article-snippet__title tm-article-snippet__title_h2').get_text(strip=True)
                if public_time.find('вчера') == 0 and not Posts.objects.filter(headline=headline):
                    Posts.objects.create(
                    headline=headline,
                    link=HOST + item.find('a', class_ = 'tm-article-snippet__title-link').get('href'),)
                    print('Появилась новая запись')
                    flag = True
            return flag


        def send_message():
            """отправить сообщение на канал"""
            # найти все боты для задачи №1
            bots = SlackBots.objects.filter(task='work1')
            for bot in bots:
                delay = bot.delay
                channel = bot.channel
                editor_text = bot.editor_text
                slackbot = WebClient(token=bot.token)
                print(bot.token)
                slackbot.chat_postMessage(channel = channel, text = editor_text)
                time.sleep(delay)
                posts = Posts.objects.filter(status='waiting')
                for post in posts:
                    link = post.link
                    SLACKBOT.chat_postMessage(channel = channel, text = link)
                    post.status = 'sended'
                    post.save()
                    print('Сообщение отправлено')
                    time.sleep (delay)


        def parse():
            """основная функция парсинга"""
            # получаем html код страницы
            html = get_html(URL)
            if html.status_code == 200: # если есть соединение:
                # Вызвать пункцию для заполнения данных
                data = get_content(html.text)
                data = True
                # Если есть новые записи:
                if data:
                    # Отправить сообщение каналу
                    send_message()
                else:
                    send_message()                    
                    print('новых постов нет')
            else:
                print('Error')
            return


        parse()
