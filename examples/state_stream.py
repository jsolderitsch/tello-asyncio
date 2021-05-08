#!/usr/bin/env python3

import asyncio
from tello_asyncio import Tello


async def main():
    drone = Tello()

    async def fly():
        await drone.takeoff()
        await drone.land()

    async def watch_state():
        async for state in drone.state_stream:
            print(f'height: {state.height}, battery: {state.battery}')     

    try:
        await drone.connect()
        await asyncio.wait([fly(), watch_state()], return_when=asyncio.FIRST_COMPLETED)
    finally:
        await drone.disconnect()

asyncio.run(main())