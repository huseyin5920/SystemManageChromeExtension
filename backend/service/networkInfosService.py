import asyncio
import json

import websockets
import psutil


class NetworkInfosService():
    async def echo(websocket, path):
        async for message in websocket:
            print(message)
            x = psutil.net_io_counters(pernic=True)
            print(json.dumps(x))

            await websocket.send(json.dumps(x))


async def main():
    async with websockets.serve(NetworkInfosService.echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
