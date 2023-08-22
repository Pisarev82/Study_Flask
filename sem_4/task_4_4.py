"""
Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте потоки.
"""
import os
import threading
import time

dir = "asyncio_"


def count_worlds_in_file(file_name, dir):
    path = os.path.join(dir, file_name)
    with open(path, "r", encoding='utf-8') as f:
        text = f.read()
        result = len(text.split(" "))
        print(f"В  {file_name} {result} слов. Посчитано за {time.time()-start_time:.2f} seconds")


threads = []
start_time = time.time()
for file_name in os.listdir(dir):
    thread = threading.Thread(target=count_worlds_in_file, args=[file_name, dir])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

