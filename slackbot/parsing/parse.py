import requests
from bs4 import BeautifulSoup


# url страницы для парсинга
URL = 'https://m.habr.com/ru/company/skillfactory/blog/'
# выдаваемый агент для сайта
HEADERS = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36',
'Accept' : '*/*'}
# хост нужно передать без слэша в конце
HOST = 'https://m.habr.com'


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
    

def parse():
    """основная функция парсинга"""

    # получаем html код страницы
    html = get_html(URL)
    if html.status_code == 200: # если есть соединение:
        get_content(html.text) # получаем требуемые объекты
    else:
        print('Error')


parse()