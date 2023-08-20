"""
Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте потоки.
"""
import os

import requests
import threading
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://netology.ru',
        'https://practicum.yandex.ru',
        'https://antiplagiat.ru',
        'https://skillbox.ru',
        'https://ru.wikipedia.org',
        'https://web.whatsapp.com/',
]


def download(url):
    response = requests.get(url)
    filename = 'threading_/' + url.replace('https://',
    '').replace('.', '_').replace('/', '') + '.html'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")


threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
