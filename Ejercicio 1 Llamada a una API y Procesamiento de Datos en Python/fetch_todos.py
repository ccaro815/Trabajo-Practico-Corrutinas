import aiohttp
import asyncio

async def fetch_todos():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/todos') as response:
            todos = await response.json()
            completed_todos = [todo['title'] for todo in todos if todo['completed']]
            for title in completed_todos:
                print(title)

asyncio.run(fetch_todos())
