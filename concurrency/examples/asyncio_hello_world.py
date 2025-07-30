import asyncio

async def main():
    await asyncio.sleep(10)
    print("Hello, there")

if __name__ == "__main__":
    asyncio.run(main())
