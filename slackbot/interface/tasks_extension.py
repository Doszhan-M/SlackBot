import requests
from bs4 import BeautifulSoup
from interface.models import Posts, SlackBots, TaskConfig
from interface.management.commands.random_agent import get_agent
from slack import WebClient
import time
from datetime import datetime


# url страницы для парсинга
URL = 'https://habr.com/ru/company/skillfactory/blog/'
# выдаваемый агент для сайта
HEADERS = {'User-Agent' : get_agent(),
'Accept' : '*/*'}
# Таймаут парсера
try:
    delay = TaskConfig.objects.filter(task='task1').order_by('-id')[0].parse_delay * 60
except IndexError:
    delay = 300


# декоратор задержки
def onceEveryXSeconds(seconds):                         
    def wrapper(f):                                       
        f.last_execution = 0                                                        
        def decorated(*args, **kwargs):                     
            if f.last_execution < time.time() - seconds:
                f.last_execution = time.time()
                return f(*args, **kwargs)
        return decorated
    return wrapper


# Декорируем функцию, чтобы применить задержку, передаем саму задержку
@onceEveryXSeconds(delay)
def get_html(url, params=None):
    """получить html код всей страницы"""
    print('получить html код всей страницы')
    # на вход принимает URL, params для парсинга пагинации
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    """создаем python объекты из спарсенной страницы"""
    # работа библиотеки BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # получаем все статьи вместе с временем публикации
    items = soup.find_all('article', class_ = 'post post_preview')
    for item in items:  
        # Получить время поста
        public_time = item.find('span', class_ = 'post__time').get_text(strip=True)
        # Получить заголовок поста
        headline=item.find('h2', class_ = 'post__title').get_text(strip=True)
        if public_time.find('31 марта') == 0 and not Posts.objects.filter(headline=headline):
            Posts.objects.create(
            headline=headline,
            link=item.find('a', class_ = 'post__title_link').get('href'),
            tags=item.find('ul', class_ = 'post__hubs inline-list').get_text(strip=True))
            print('Появилась новая запись')
        else:
            print('Новых постов нет') 


def send_message():
    """отправить сообщение на канал"""
    # найти все собранные посты за период №1
    posts = Posts.objects.filter(status='waiting')
    if posts:
        # найти все боты для задачи №1
        bots = SlackBots.objects.filter(task='work1')
        for bot in bots:
            delay = bot.delay
            channel = bot.channel
            editor_text = bot.editor_text
            slackbot = WebClient(token=bot.token)
            slackbot.chat_postMessage(channel = channel, text = editor_text)
            time.sleep(delay)
            # отправить все посты с задержкой
            for post in posts:
                link = post.link
                slackbot.chat_postMessage(channel = channel, text = link)
                # изменить статус поста на отправлено
                post.status = 'sended'
                post.save()
                print('Сообщение отправлено')
                time.sleep (delay)
    else:
        print('Ожидание новых постов')


def work_mode(mode):
    """режим работы отправки сообщения"""
    if mode == 'mode1':
        send_message()
    elif mode == 'mode2':
        minute = TaskConfig.objects.filter(name='task1').order_by('-id')[0].minute
        if datetime.now().minute == minute:
            send_message()
    elif mode == 'mode3':
        hour = TaskConfig.objects.filter(name='task1').order_by('-id')[0].hour
        if datetime.now().hour == hour:
            send_message()
    elif mode == 'mode4':
        day = TaskConfig.objects.filter(name='task1').order_by('-id')[0].day
        if datetime.now().isoweekday() == day:
            send_message()


def work_mode2(mode):
    """режим работы отправки сообщения"""
    if mode == 'mode1':
        send_message2()
    elif mode == 'mode2':
        minute = TaskConfig.objects.filter(name='task1').order_by('-id')[0].minute
        if datetime.now().minute == minute:
            send_message2()
    elif mode == 'mode3':
        hour = TaskConfig.objects.filter(name='task1').order_by('-id')[0].hour
        if datetime.now().hour == hour:
            send_message2()
    elif mode == 'mode4':
        day = TaskConfig.objects.filter(name='task1').order_by('-id')[0].day
        if datetime.now().isoweekday() == day:
            send_message2()



def send_message2():
    """отправить сообщение на канал"""
    # найти все собранные посты за период задачи №2
    posts = Posts.objects.filter(status='waiting')
    text = set()
    if posts:
        # найти все боты для задачи №2
        bots = SlackBots.objects.filter(task='work2')
        for bot in bots:
            delay = bot.delay
            channel = bot.channel
            editor_text = bot.editor_text
            slackbot = WebClient(token=bot.token)
            # Из постов и ботов достаем теги, и сравниваем их
            for post in posts:
                tags = post.tags.lower().split(',')
                bot_tags = bot.bot_tags.lower().replace(', ', ',').split(',')
                for i in tags:
                    if i in bot_tags:
                        # Если есть совпадение, то добавляем ее в переменную
                        link = post.link
                        text.add(link)
                # изменить статус поста на отправлено
                post.status = 'sended'
                post.save()
    if text:
        # текс редактора
        slackbot.chat_postMessage(channel = channel, text = editor_text)
        time.sleep (delay)
        for i in text:
            # отправить все посты с задержкой
            slackbot.chat_postMessage(channel = channel, text = i)
            print('Сообщение отправлено')
            time.sleep (delay)
    else:
        print('Ожидание новых постов')


def get_agent():
    """передавать рандомный агент во избежание бана"""
    agent_strings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
    return random.choice(agent_strings)