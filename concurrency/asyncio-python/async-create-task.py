import asyncio

async def coro(numbers):
    await asyncio.sleep(min(numbers))
    return list(reversed(numbers))

async def do_something():
    task = asyncio.create_task(coro([1, 2, 3]))
    print(f"{type(task) = }")
    print(f"{task.done() = }")
    return await task

async def main():
    result = await do_something()
    print(f"{result = }")

asyncio.run(main())

