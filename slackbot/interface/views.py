from django.views.generic import TemplateView, CreateView
from .forms import SlackBotForm, ParseForm
from .models import TaskConfig
from django.urls import reverse_lazy
from django.shortcuts import redirect
import subprocess
from .tasks import parse
from django.http import HttpResponseRedirect
from celery.contrib.abortable import AbortableAsyncResult
from slackbot.celery import app
from django.contrib import messages
from datetime import datetime


class BotConfig(CreateView):
    form_class = SlackBotForm
    template_name = 'interface/botconfig.html'
    success_url = reverse_lazy('botconfig')


class ParseConfig(CreateView):
    form_class = ParseForm
    template_name = 'interface/parseconfig.html'
    success_url = reverse_lazy('start_bot')


def start_bot(request):
    """старт задачи №1"""
    # Определить режим работы и передать в задачу
    mode = TaskConfig.objects.filter(name='task1').order_by('-id')[0].mode
    # Запустить задачу #1
    task = parse.delay(mode)
    # Сохранить ид задачи в базу
    config = TaskConfig.objects.filter(name='task1').order_by('-id')[0]
    config.task_id = task.id
    config.save()
    
    
    return redirect('botconfig')


def stop_bot(request):
    """стоп задачи №1"""
    task_id = TaskConfig.objects.filter(name='task1').order_by('-id')[0].task_id
    app.control.revoke(task_id, terminate=True)
    messages.error(request, 'Задача остановлена!')
    return redirect('botconfig')


def stop_all_bots(request):
    """стоп всех задач"""
    task_ids = TaskConfig.objects.filter(name='task1')
    for task_id in task_ids:
        app.control.revoke(task_id.task_id, terminate=True)
    messages.error(request, 'Задача остановлена!')
    return redirect('botconfig')
