import asyncio

async def async_sleep():
    print('Before sleep')
    print('Sleeping...')
    await asyncio.sleep(5)
    print('After sleep')
    
async def return_hello():
    return 'Hello'
    
async def main():
    await async_sleep()
    result = await return_hello()
    print(result)
    
if __name__=="__main__":
    asyncio.run(main())