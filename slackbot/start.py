# import subprocess

#     # отрыть скрипт bash как файл и выполнить ее из python среды
#     with open('./scripts/parse.sh', 'rb') as file:
#         script = file.read()
#     rc = subprocess.call(script, shell=True)
#     return redirect('botconfig')
import requests
from bs4 import BeautifulSoup


# url страницы для парсинга
URL = 'https://habr.com/ru/company/skillfactory/blog/'
# выдаваемый агент для сайта
HEADERS = {'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
'Accept' : '*/*'}
# хост нужно передать без слэша в конце
HOST = 'https://habr.com'


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
    
    a = []
    items = soup.find_all('article', class_ = 'post post_preview')
    
    for item in items:  
        # Получить время поста
        public_time = item.find('span', class_ = 'post__time').get_text(strip=True)
        # Получить заголовок поста
        headline = item.find('h2', class_ = 'post__title').get_text(strip=True)
        link = item.find('a', class_ = 'post__title_link').get('href')
        tags = item.find('ul', class_ = 'post__hubs inline-list').get_text(strip=True).lower().split(',')
        print(tags)
            

    return 

def parse():
    html = get_html(URL)
    if html.status_code == 200:  # если есть соединение:
        get_content(html.text) 

parse()