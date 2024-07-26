import asyncio
import time
import requests
import aiohttp
import ssl
import certifi

async def get_url_response(url):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=ssl_context) as response:
            return await response.text()

async def main():
    urls = [
        'https://google.com',
        'https://www.wikipedia.org',
        'https://www.example.com',
        'https://www.w3schools.com',
        'https://developer.mozilla.org',
        'https://stackoverflow.com',
        'https://github.com',
        'https://www.bbc.com',
        'https://www.cnn.com',
        'https://www.openai.com'
    ]

    # Synchronous requests
    start = time.time()
    sync_text_responses = []
    for url in urls:
        sync_text_responses.append(requests.get(url).text)
    sync_end_time = time.time()
    print('Synchronous requests took: ', sync_end_time - start)

    # Asynchronous requests
    start = time.time()
    tasks = [get_url_response(url) for url in urls]
    async_text_responses = await asyncio.gather(*tasks)
    async_end_time = time.time()
    print('Asynchronous requests took: ', async_end_time - start)

if __name__ == "__main__":
    asyncio.run(main())
