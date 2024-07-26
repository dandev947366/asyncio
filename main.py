import asyncio
import time
async def async_sleep(n):
    print(f'Before sleep {n}')
    print('Sleeping...')
    await asyncio.sleep(5)
    print(f'After sleep {n}')
    
async def print_hello():
    print('Hello')
    
  
async def main():
    start = time.time()
    # task = asyncio.create_task(async_sleep(1)) 
    # await async_sleep(2)
    # await task
    # await print_hello()
    try:
        await asyncio.gather(asyncio.wait_for(async_sleep(30), 5), async_sleep(6), print_hello())
    except asyncio.TimeoutError:
        print('Encountered timeout error')
    print('total time: ', time.time() - start)
    
if __name__=="__main__":
    asyncio.run(main())