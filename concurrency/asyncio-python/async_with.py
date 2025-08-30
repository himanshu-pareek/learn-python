import asyncio
import aiohttp

async def check_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url} [ status: {response.status}]")

async def main():
    websites = [
            "https://realpython.com",
            "https://pycoders.com",
            "https://python.org",
    ]

    await asyncio.gather(*(check_url(website) for website in websites))

asyncio.run(main())


