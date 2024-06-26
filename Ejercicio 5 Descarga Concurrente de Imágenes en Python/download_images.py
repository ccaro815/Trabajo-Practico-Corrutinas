import aiohttp
import asyncio
import os

image_urls = [
    'https://example.com/image1.jpg',
    'https://example.com/image2.jpg',
]

async def download_image(session, url, folder):
    async with session.get(url) as response:
        image_data = await response.read()
        filename = os.path.join(folder, os.path.basename(url))
        with open(filename, 'wb') as f:
            f.write(image_data)

async def download_images(image_urls, folder='images'):
    os.makedirs(folder, exist_ok=True)
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, folder) for url in image_urls]
        await asyncio.gather(*tasks)

asyncio.run(download_images(image_urls))
