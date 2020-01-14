import time
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 1
async def fetch_async(session, pid):
    print('Fetch async process {} started'.format(pid))
    start = time.time()
    async with session.get(URL) as response:
        datetime = response.headers.get('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))
    response.close()
    return datetime


async def asynchronous():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(
            fetch_async(session, i)) for i in range(1, MAX_CLIENTS + 1)]
        await asyncio.wait(tasks)
    print("Process took: {:.2f} seconds".format(time.time() - start))

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
