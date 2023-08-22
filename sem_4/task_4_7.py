"""
� Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами
от 1 до 100.
� При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения
вычислений.
"""
import multiprocessing
import random
import time
import threading
from multiprocessing import Process, Manager

number_of_threading = number_of_process = number_of_asyncio = 4


def arr_generate():
    start_time = time.time()
    print(f"Start")
    arr = [random.randint(1, 100) for _ in range(10_000_000)]
    print(f"arr generate at {time.time() - start_time:.2f} seconds")
    return arr


def sum_of_arr(arr: list):
    result = 0
    for i in arr:
        result += i
    return result


def sum_of_arr_for_threads(arr: list, result:list):
    for i in arr:
        result[0] += i



def sum_of_arr_threads(arr: list):
    threads = []
    result_of_threads = [0]
    chunk_size = int(len(arr)/number_of_process)
    for i in range(0, len(arr), chunk_size):
        chunk = arr[i:i + chunk_size]
        thread = threading.Thread(target=sum_of_arr_for_threads, args=[chunk, result_of_threads])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return result_of_threads[0]


def sum_of_arr_for_multiprocessing(arr: list, start_position, chunk_size, result_out):
    result = 0
    for each in arr[start_position:start_position + chunk_size]:
        result += each
    print(f"Значение счетчика: {result:_}")
    result_out[str(start_position)] = result


if __name__ == '__main__':
    arr_ = arr_generate()

    start_time = time.time()
    print(f"Встроенный метод sum {sum(arr_):_} Посчитано за {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    print(f"Последовательный подсчет {sum_of_arr(arr_):_} Посчитано за {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    print(f"Подсчет в потоках Thread {sum_of_arr_threads(arr_):_} Посчитано за {time.time() - start_time:.2f} seconds")
    start_time = time.time()

    processes = []
    processes_result = 0
    with Manager() as manager:
        chunk_size = int(len(arr_) / number_of_process)
        processes_result_in = manager.dict()
        for i in range(0, len(arr_), chunk_size):
            # chunk = arr[i:i+chunk_size]
            process = Process(target=sum_of_arr_for_multiprocessing, args=(arr_, i, chunk_size, processes_result_in))
            processes.append(process)
            print(f"Процесс {i} запущен   за {time.time() - start_time:.2f} seconds")
            process.start()

        for process in processes:
            process.join()
        processes_result = sum(processes_result_in.values())
    print(f"Подсчет в процессах Process {processes_result:_} Посчитано за {time.time() - start_time:.2f} seconds")
