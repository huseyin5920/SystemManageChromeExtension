#!/usr/bin/env python

import asyncio
import time

import websockets


async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        return await websocket.recv()

while True:
    x = asyncio.run(hello())
    time.sleep(3)
    print(x)
