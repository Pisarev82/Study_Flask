"""
� Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
� Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
� Программа должна использовать многопоточный, многопроцессорный и
асинхронный подходы.
� Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
� Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы.
"""
import aiofiles
import aiohttp
# import os
#
# import aiofiles
# import aiohttp
#
#
#



import requests
import os
import time
import threading
import multiprocessing
import asyncio
import argparse


# Функция для скачивания изображения
def download_image(url, output_dir):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(output_dir, os.path.basename(url))
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Изображение {url} успешно скачано и сохранено в {filename}")
    else:
        print(f"Не удалось скачать изображение {url}")


# Функция для запуска скачивания в отдельном потоке
def download_image_thread(url, output_dir):
    start_time = time.time()
    download_image(url, output_dir)
    end_time = time.time()
    print(f"Время скачивания изображения {url}: {end_time - start_time} секунд")


# Функция для запуска скачиваний в отдельном потоке
def download_images_thread(urls, output_dir):
    threads = []
    start_time = time.time()
    for url in urls:
        thread = threading.Thread(target=download_image_thread, args=[url, output_dir])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Время скачивания изображений в потоке : {time.time() - start_time} секунд")


# Функция для запуска скачивания в отдельном процессе
def download_image_process(url, output_dir):
    start_time = time.time()
    download_image(url, output_dir)
    end_time = time.time()
    print(f"Время скачивания изображения {url}: {end_time - start_time} секунд")


def download_images_process(urls, output_dir):
    processes = []
    start_time = time.time()
    for url in urls:
        process = multiprocessing.Process(target=download_image_process, args=(url, output_dir))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print(f"Время скачивания изображений в процессах : {time.time() - start_time} секунд")


# Функция для запуска скачивания асинхронно
async def download_image_async(url, output_dir):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()

    filename = os.path.join(output_dir, os.path.basename(url))

    async with aiofiles.open(filename, 'wb') as f:
        await f.write(content)
    end_time = time.time()
    print(f"Время скачивания изображения {url}: {end_time - start_time} секунд")


# Функция для запуска скачивания изображений асинхронно
async def download_images_async(urls, output_dir):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_image_async(url, output_dir))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f"Время скачивания изображений асинхронно {time.time() - start_time} секунд")


if __name__ == '__main__':
    """
    Запуск через терминал. Пример команды для запуска. В примере все ссылки рабочие:
    
    python task_4_9.py https://klike.net/uploads/posts/2023-01/1674707917_1.jpg https://w-dog.ru/wallpapers/16/16/313072689307185/sobaki-priroda-fon.jpg https://kartinkin.net/pics/uploads/posts/2022-07/1657835782_9-kartinkin-net-p-poroda-sobak-akita-zhivotnie-krasivo-foto-9.jpg https://phonoteka.org/uploads/posts/2021-07/1625747347_17-phonoteka-org-p-akita-inu-art-krasivo-18.jpg
    
    """
    # Получение списка URL-адресов через аргументы командной строки
    """
    Можно закоментировать следующий код и раскоментировать список если нет желания запускать код из терминала
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('urls', nargs='+', help='Список URL-адресов для скачивания')
    args = parser.parse_args()
    image_urls = args.urls

    """ Можно раскоментировать список если нет желания запускать код из терминала"""
    # image_urls = [
    #     'https://klike.net/uploads/posts/2023-01/1674707917_1.jpg',
    #     'https://w-dog.ru/wallpapers/16/16/313072689307185/sobaki-priroda-fon.jpg',
    #     'https://kartinkin.net/pics/uploads/posts/2022-07/1657835782_9-kartinkin-net-p-poroda-sobak-akita-zhivotnie-krasivo-foto-9.jpg',
    #     'https://phonoteka.org/uploads/posts/2021-07/1625747347_17-phonoteka-org-p-akita-inu-art-krasivo-18.jpg',
    # ]

    # Создание директории для сохранения изображений
    output_dir = 'images'
    os.makedirs(output_dir, exist_ok=True)

    #Выполнение в потоках
    # download_images_thread(image_urls, output_dir)

    # Выполнение в процессах
    # download_images_process(image_urls, output_dir)

    # Выполнение асинхронно
    asyncio.run(download_images_async(image_urls, output_dir))

