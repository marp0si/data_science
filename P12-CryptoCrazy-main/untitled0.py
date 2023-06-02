# -*- coding: utf-8 -*-
"""
Created on Sun May 28 10:42:10 2023

@author: PC
"""
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_forever()