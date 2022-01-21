import asyncio
import json

import websockets
import psutil


class CpuInfosService():
    async def echo(websocket, path):
        async for message in websocket:
            print(message)
            print('The CPU usage is: ', psutil.cpu_percent(interval=1))
            while True:
                await websocket.send(str(psutil.cpu_percent(interval=1)))


async def main():
    async with websockets.serve(CpuInfosService.echo, "0.0.0.0", 8767):
        await asyncio.Future()  # run forever

asyncio.run(main())
