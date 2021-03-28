from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from interface.models import Posts, SlackBots


class Command(BaseCommand):
    help = 'Оповещать сотрудников SF в Slack о выходе всех новых статей по всем тематикам в блоге компании на habr'

    def handle(self, *args, **options):

        # url страницы для парсинга
        URL = 'https://m.habr.com/ru/company/skillfactory/blog/'
        # выдаваемый агент для сайта
        HEADERS = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36',
        'Accept' : '*/*'}
        # хост нужно передать без слэша в конце
        HOST = 'https://m.habr.com'
        FLAG = 3 #отладка


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
            # список словарей для наполнения данными публикации
            posts = []
            for item in items:
                posts.append({
                    'header' : item.find('h2', class_ = 'tm-article-snippet__title tm-article-snippet__title_h2').get_text(strip=True),
                    'time' : item.find('span', class_ = 'tm-article-snippet__datetime-published').get_text(strip=True),
                    'link' : HOST + item.find('a', class_ = 'tm-article-snippet__title-link').get('href'),
                })
            return posts
            

        def get_pages_count(html):
            """получить количество страниц"""

            soup = BeautifulSoup(html, 'html.parser')
            # получить все номера страницы
            pagination = soup.find_all('a', class_ = 'tm-pagination__page')
            # вернуть номер последней страницы
            return int(pagination[-1].get_text(strip=True))


        def parse():
            """основная функция парсинга"""

            # получаем html код страницы
            html = get_html(URL)
            if html.status_code == 200: # если есть соединение:
                if FLAG == 1:
                    posts = [] # список постов с данными
                    pages_count = get_pages_count(html.text) # получаем количество страниц
                    pages_count = 2 # отладка
                    for page in range(1, pages_count + 1):
                        print(f'Парсинг страницы {page} из {pages_count}')
                        page = 'page' + str(page)
                        html = get_html(URL, params={'page': page}) # получить html код каждой страницы
                        posts.extend(get_content(html.text)) # дополняем список данными со всех страниц
                    print(posts)  
                elif FLAG == 2:    
                    posts = get_content(html.text) # получаем требуемые объекты из первой страницы
                elif FLAG == 3:  
                    posts = get_content(html.text)
                    print(posts)
            else:
                print('Error')


        parse()