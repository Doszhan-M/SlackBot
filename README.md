# SLACKBOT for SkillFactory
![picture](https://miro.medium.com/max/4000/1*AB7mUaMbKwZjThYXVIuenQ.jpeg)

Внимательно прочтите инструкцию перед развертыванием приложения!


Приложение для работы использует библиотеки Celery и Redis они не корректно работают на Windows, поэтому крайне рекомендуется использовать ос Ubuntu. 

1. Установите в систему Redis:\
$ sudo apt-get update\
$ sudo apt-get install redis\
затем запустите его:\
$ redis-server

2. Создайте виртуальное окружение и установите необходимые пакеты для работы приложения:\
pip3 install -r requirements.txt\
Дождитесь окончания установки всех зависимостей.

3. Из корня проекта запустите сервер. Корнем считается тот каталог, где находиться файл manage.py:
* python3 manage.py runserver

4. Из корня проекта запустите Celery:
* celery -A slackbot worker -l INFO\

5. Откройте браузер и перейдите на адрес:
* http://127.0.0.1:8000/

На этом приложение запущено и готово к установке.