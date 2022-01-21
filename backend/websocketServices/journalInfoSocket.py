import select
from systemd import journal
import asyncio
import json
import websockets
import psutil


j = journal.Reader()
j.log_level(journal.LOG_INFO)

j.seek_tail()
j.get_previous()

p = select.poll()
p.register(j, j.get_events())




class NetworkInfosService():
    async def echo(websocket, path):
        async for message in websocket:
            print(message)
            while p.poll():
                if j.process() != journal.APPEND:
                    continue
                for entry in j:
                    if entry['MESSAGE'] != "":
                        print(str(entry['__REALTIME_TIMESTAMP'] )+ ' ' + entry['MESSAGE'])
                        await websocket.send(str(entry['__REALTIME_TIMESTAMP'] )+ ' ' + entry['MESSAGE'])
                   


async def main():
    async with websockets.serve(NetworkInfosService.echo, "0.0.0.0", 8766,ping_interval=None, ping_timeout=None):
        await asyncio.Future()  # run forever

asyncio.run(main())







