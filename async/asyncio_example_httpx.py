# Пример ассинхронных запросов с использованием httpx
import httpx
import asyncio
import time

async def async_pull(url):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)


async def build_task() -> None:
  goog_fin_nyse_url = 'https://www.google.com/finance/quote/'
  url = goog_fin_nyse_url + '' + ':NYSE'
  tasks = [asyncio.create_task(async_pull(url)) for i in range(300)]
  start_time = time.time()
  await asyncio.gather(*tasks)

  finish_time = time.time()
  elapsed_time = finish_time - start_time
  print(f"\n Time spent processing: {elapsed_time} ")


if __name__ == "__main__":
  asyncio.run(build_task())
