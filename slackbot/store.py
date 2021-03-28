def get_pages_count(html):
    """получить количество страниц"""
    soup = BeautifulSoup(html, 'html.parser')
     # получить все номера страницы
    pagination = soup.find_all('a', class_ = 'tm-pagination__page')
    # вернуть номер последней страницы
    return int(pagination[-1].get_text(strip=True))


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