from celery import shared_task
import requests
from bs4 import BeautifulSoup
from interface.models import Posts, SlackBots, TaskConfig
from interface.tasks_extension import get_html, URL, get_content, send_message, work_mode
from slack import WebClient
import time
from celery.contrib.abortable import AbortableTask
from slackbot.celery import app


@app.task(bind=True, base=AbortableTask)
@shared_task
def parse(mode):
    """Оповещать сотрудников SF в Slack о выходе всех новых статей по всем тематикам в блоге компании на habr"""
    while True:
        # получаем html код страницы
        html = get_html(URL)
        try:
            if html.status_code == 200:  # если есть соединение:
                get_content(html.text)   # Вызвать функцию для заполнения данных
        except AttributeError:
            work_mode()  # Вызвать функцию для отправки сообщения в слак
            time.sleep(1)  # задержка для стабильности
