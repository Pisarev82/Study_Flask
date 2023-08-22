"""
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте асинхронный подход.
"""
import os
import asyncio
import time

import aiofiles as aiofiles

dir = "threading_"


async def count_worlds_in_file(file_name, dir):
    path = os.path.join(dir, file_name)
    async with aiofiles.open(path, 'r', encoding='utf-8') as f:
        text = await f.read()
    result = len(text.split(" "))
    print(f"В  {file_name} {result} слов. Посчитано за {time.time()-start_time:.2f} seconds")


async def main():
    tasks = []
    for file_name in os.listdir(dir):
        task = asyncio.create_task(count_worlds_in_file(file_name, dir))
        # task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())

    print(f"Посчитано за {time.time()-start_time:.2f} seconds")