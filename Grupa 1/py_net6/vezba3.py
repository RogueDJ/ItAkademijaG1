import asyncio, time

async def uradi():
    for i in range(10):
        print(f"Ja nesto radim {i}")
        await asyncio.sleep(1)

async def main():
    t1 = asyncio.create_task(uradi())

asyncio.run(main())