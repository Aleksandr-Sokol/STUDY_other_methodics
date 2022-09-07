# Пример ассинхронных запросов с использованием aiohttp
import asyncio
import aiohttp
import datetime


async def fetch_context(url, session, info):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        await asyncio.sleep(0)


async def main_2():
    info = '123'
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_context('https://ya.ru', session, info)) for i in range(300)]
        await asyncio.gather(*tasks)


t0 = datetime.datetime.now()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main_2())
print(datetime.datetime.now() - t0)
