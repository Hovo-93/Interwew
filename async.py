import asyncio
import aiohttp

URLS = ['http://127.0.0.1:8000/product/1/', 'http://127.0.0.1:8000/product/2/']


async def main():
    async with aiohttp.ClientSession() as session:
        for url in URLS:
            print(url)
            async with session.get(url) as response:
                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                html = await response.text()
                file = open("data.txt", "w")
                file.write(f'{html}')
                file.close()
                print("Body:", html[:15], "...")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
