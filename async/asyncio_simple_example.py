# Простейший пример работы ассинхронных програм
# Конкурентный доступ к ресурсам
import asyncio
import datetime


async def fetch_context1():
    print(f'start fetch_context1 {datetime.datetime.now().strftime("%H:%M:%S")}')
    await asyncio.sleep(5)
    print(f'stop fetch_context1 {datetime.datetime.now().strftime("%H:%M:%S")}')


async def fetch_context2():
    print(f'start fetch_context2 {datetime.datetime.now().strftime("%H:%M:%S")}')
    await asyncio.sleep(5)
    print(f'stop fetch_context2 {datetime.datetime.now().strftime("%H:%M:%S")}')


async def fetch_context3():
    print(f'start fetch_context3 {datetime.datetime.now().strftime("%H:%M:%S")}')
    await asyncio.sleep(5)
    print(f'stop fetch_context3 {datetime.datetime.now().strftime("%H:%M:%S")}')


async def main_2():
    queue = asyncio.Queue()
    print(queue)
    print(f'start main {datetime.datetime.now().strftime("%H:%M:%S")}')
    await queue.join()
    await asyncio.gather(
        asyncio.create_task(fetch_context1()),
        asyncio.create_task(fetch_context2()),
        asyncio.create_task(fetch_context3()),
    )
    print(f'stop main {datetime.datetime.now().strftime("%H:%M:%S")}')


loop = asyncio.new_event_loop()
loop.run_until_complete(main_2())
# или
# asyncio.run(main_2())