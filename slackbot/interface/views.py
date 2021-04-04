from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from .forms import SlackBotForm, ParseForm
from .models import TaskConfig, SlackBots
from django.urls import reverse_lazy
from django.shortcuts import redirect
import subprocess
from .tasks import parse, parse2
from django.http import HttpResponseRedirect
from celery.contrib.abortable import AbortableAsyncResult
from slackbot.celery import app
from django.contrib import messages
from datetime import datetime


class BotConfig(CreateView, ListView,):
    form_class = SlackBotForm
    template_name = 'interface/botconfig.html'
    success_url = ('#portfolio')

    model = SlackBots
    context_object_name = 'bot_list'

    def post(self, request, *args, **kwargs):
        post = super().post(request, *args, **kwargs)
        messages.info(request, 'SlackBot успешно создан!')
        return post


class ParseConfig(CreateView):
    form_class = ParseForm
    template_name = 'interface/parseconfig.html'
    success_url = reverse_lazy('start_bot')

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательно
        fields.task = 'task1'
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)


class ParseConfig2(CreateView):
    form_class = ParseForm
    template_name = 'interface/parseconfig2.html'
    success_url = reverse_lazy('start_bot2')

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательно
        fields.task = 'task2'
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)


class BotDelete(DeleteView):
    template_name = 'interface/botdelete.html'
    queryset = SlackBots.objects.all()
    success_url = reverse_lazy('botconfig')


class BotEdit(UpdateView):
    template_name = 'interface/botedit.html'
    form_class = SlackBotForm
    queryset = SlackBots.objects.all()
    success_url = reverse_lazy('botconfig')


def start_bot(request):
    """старт задачи №1"""
    # Определить режим работы и передать в задачу
    task_num = 'task1'
    status = 'waiting1'
    task = TaskConfig.objects.filter(task=task_num).order_by('-id')[0]
    mode = task.mode  
    # Запустить задачу #1
    celery_task = parse.delay(mode, task_num, status)
    # Сохранить ид задачи в базу    
    task.task_id = celery_task.id
    task.save()
    messages.info(request, 'Задача успешно запущена!')
    return redirect('botconfig')


def start_bot2(request):
    """старт задачи №2"""
    # Определить режим работы и передать в задачу
    task_num = 'task2'
    status = 'waiting2'
    task = TaskConfig.objects.filter(task=task_num).order_by('-id')[0]
    mode = task.mode  
    # Запустить задачу #1
    celery_task = parse.delay(mode, task_num, status)
    # Сохранить ид задачи в базу    
    task.task_id = celery_task.id
    task.save()
    messages.info(request, 'Задача успешно запущена!')
    return redirect('botconfig')


def stop_bot(request):
    """стоп задачи №1"""
    if request.GET["bot_type"] == "1":
        task = 'task1'
        print(task)
    else:
        task = 'task2'
        print(task)
    task_id = TaskConfig.objects.filter(task=task).order_by('-id')[0].task_id
    app.control.revoke(task_id, terminate=True)
    messages.info(request, 'Задача остановлена!')
    return redirect('botconfig')


def stop_all_tasks(request):
    """стоп всех задач"""
    task_ids = TaskConfig.objects.all()
    for task_id in task_ids:
        app.control.revoke(task_id.task_id, terminate=True)
    messages.info(request, 'Задачи остановлены!')
    return redirect('botconfig')


