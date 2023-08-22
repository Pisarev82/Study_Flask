"""
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте процессы.
"""
import os
from multiprocessing import Process, Pool
import time

dir = "asyncio_"


def count_worlds_in_file(file_name, dir):
    path = os.path.join(dir, file_name)
    with open(path, "r", encoding='utf-8') as f:
        text = f.read()
        result = len(text.split(" "))
        print(f"В  {file_name} {result} слов. Посчитано за {time.time()-start_time:.2f} seconds")


processes = []
start_time = time.time()

if __name__ == '__main__':

    for file_name in os.listdir(dir):
        process = Process(target=count_worlds_in_file, args=(file_name, dir))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Посчитано за {time.time()-start_time:.2f} seconds")
