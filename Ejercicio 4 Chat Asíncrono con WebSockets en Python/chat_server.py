import asyncio
import websockets

connected_clients = set()

async def chat_handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await asyncio.wait([client.send(message) for client in connected_clients])
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(chat_handler, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
