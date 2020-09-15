from bs4 import BeautifulSoup
import requests
import random
import time
urls=[]
lifehacker = []

def newsletter():
    s = requests.Session()
    headers = {
    'Accept' : '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    url = 'https://zen.yandex.ru/different_angle?clid=300&token='
    request = s.get(url, headers=headers)
    pages_content = BeautifulSoup(request.content, 'html.parser')
    array_notes = pages_content.find_all('a', attrs={'class': 'card-image-view__clickable'})
    for url in array_notes:
        data = url.attrs['href']
        urls.append(data)
    return urls
def get_article(lists):
    max_len= len(lists)-1
    if max_len > 0:
        number = random.randint(0,max_len)
        return f'{lists[number]}'
    else: return f'какие-то проблемы с доступом к сайту'

def lifehacker_top_of_week():
    s = requests.Session()
    headers = {
    'Accept' : '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    url = 'https://lifehacker.ru/top/week/'
    request = s.get(url, headers=headers)
    pages_content = BeautifulSoup(request.content, 'html.parser')
    array_notes = pages_content.find_all('div', attrs= {'class': 'col-sm-16'})
    for url in array_notes:
        data = url.find('a')['href']
        lifehacker.append(data)
    return lifehacker