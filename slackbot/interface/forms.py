from django.forms import ModelForm
from .models import SlackBots, TaskConfig
from django.forms import Select, TextInput, Textarea, URLInput, NumberInput


# Создаём модельную форму
class SlackBotForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. 
    class Meta:
        model = SlackBots
        fields = ['name', 'token', 'channel', 'task', 'delay', 'editor_text',]

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название бота'
            }),
            'token': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Токен слак бота'
            }),
            'url': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка страницы парсинга'
            }),
            'host': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Хост страницы'
            }),
            'channel': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Канал бота'
            }),
            'task': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Номер задачи'
            }),
            'delay': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задержка для бота'
            }),
            'editor_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вступительный текст сообщения...'
            }),

        }


# Создаём модельную форму
class ParseForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. 
    class Meta:
        model = TaskConfig
        fields = ['parse_delay', 'mode', 'minute', 'hour', 'day',]

        widgets = {
            'parse_delay': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задержка в минутах между запросами на сайт'
            }),
            'mode': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Режим работы'
            }),
            'minute': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задержка в минутах между запросами на сайт'
            }),
            'hour': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задержка в минутах между запросами на сайт'
            }),
            'day': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задержка в минутах между запросами на сайт'
            }),
        }