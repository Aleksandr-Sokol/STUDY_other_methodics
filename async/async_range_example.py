# Асинхроннуая итерация по диапазону (range)

import asyncio


async def async_range(start: int, stop: int, iter: int):
    # Ассинхронный генератор
    for i in range(start, stop, iter):
        yield(i)
        await asyncio.sleep(0.0)   # необходимо для отказа от управления


async def print_range(start: int, stop: int, iter: int):
    # Проход по ассинхроненому генератору и вывод числа
    async for i in async_range(start, stop, iter):
        # У for должно быть async, иначе ошибка 'async_generator' object is not iterable
        print(i)


async def main_2():
    # сборка очереди
    tasks = [
        asyncio.create_task(print_range(1, 10, 1)),
        asyncio.create_task(print_range(100, 110, 1)),
    ]
    await asyncio.gather(*tasks)

# Запуск
asyncio.run(main_2())
