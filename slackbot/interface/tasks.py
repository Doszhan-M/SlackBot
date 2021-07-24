import time
from celery import shared_task
from celery.contrib.abortable import AbortableTask
from interface.tasks_extension import get_html, URL, get_content, work_mode, work_mode2
from slackbot.celery import app



@app.task(bind=True, base=AbortableTask)
@shared_task
def parse(mode, task, status):
    """Оповещать сотрудников SF в Slack о выходе всех новых статей по всем тематикам в блоге компании на habr"""
    while True:
        # получаем html код страницы
        html = get_html(URL)
        try:
            if html.status_code == 200:  # если есть соединение:
                get_content(html.text, task, status)   # Вызвать функцию для заполнения данных
                work_mode(mode) 
        except AttributeError:
            work_mode(mode)  # Вызвать функцию для отправки сообщения в слак
            time.sleep(1)  # задержка для стабильности


@app.task(bind=True, base=AbortableTask)
@shared_task
def parse2(mode, task, status):
    """Оповещение учеников SkillFactory о выходе статей на habr, помеченных определенными тегами"""
    while True:
        # получаем html код страницы
        html = get_html(URL)
        try:
            if html.status_code == 200:  # если есть соединение:
                get_content(html.text, task, status)   # Вызвать функцию для заполнения данных
                work_mode2(mode) 
        except AttributeError:
            work_mode2(mode)  # Вызвать функцию для отправки сообщения в слак
            time.sleep(1)  # задержка для стабильности