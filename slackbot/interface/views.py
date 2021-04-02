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
    success_url = reverse_lazy('botconfig')

    model = SlackBots
    context_object_name = 'bot_list'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     task = parse.delay
    #     config = TaskConfig.objects.filter(name='task1').order_by('-id')[0].task_id
    #     print(f"id={task.id}, state={task.state}, status={task.status}")
    #     return context



class ParseConfig(CreateView):
    form_class = ParseForm
    template_name = 'interface/parseconfig.html'
    success_url = reverse_lazy('start_bot')


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
    mode = TaskConfig.objects.filter(task='task1').order_by('-id')[0].mode
    # Запустить задачу #1
    task = parse.delay(mode)
    # Сохранить ид задачи в базу
    config = TaskConfig.objects.filter(task='task1').order_by('-id')[0]
    config.task_id = task.id
    config.save()
    messages.info(request, 'Задача успешно запущена!')
    return redirect('botconfig')


def stop_bot(request):
    """стоп задачи №1"""
    task_id = TaskConfig.objects.filter(task='task1').order_by('-id')[0].task_id
    app.control.revoke(task_id, terminate=True)
    messages.info(request, 'Задача остановлена!')
    return redirect('botconfig')


def stop_all_bots(request):
    """стоп всех задач"""
    task_ids = TaskConfig.objects.filter(task='task1')
    for task_id in task_ids:
        app.control.revoke(task_id.task_id, terminate=True)
    messages.info(request, 'Задачи остановлены!')
    return redirect('botconfig')


def start_bot2(request):
    """старт задачи №1"""
    # Определить режим работы и передать в задачу
    mode = TaskConfig.objects.filter(task='task2').order_by('-id')[0].mode
    # Запустить задачу #1
    task = parse2.delay(mode)
    # Сохранить ид задачи в базу
    config = TaskConfig.objects.filter(task='task2').order_by('-id')[0]
    config.task_id = task.id
    config.save()
    messages.info(request, 'Задача успешно запущена!')
    return redirect('botconfig')