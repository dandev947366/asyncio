import asyncio
import multiprocessing

class MultiprocessingAsync(multiprocessing.Process):
    def __init__(self, durations):
        super(MultiprocessingAsync, self).__init__()
        self.durations = durations
        
    @staticmethod
    async def async_sleep(duration):
        await asyncio.sleep(duration)
        return duration
        
    async def consecutive_sleeps(self):
        pending = set()
        for duration in self.durations:
            pending.add(asyncio.create_task(self.async_sleep(duration)))
        while pending:
            done, pending = await asyncio.wait(pending, timeout=1)
            for done_task in done:
                print(await done_task)
                
    def run(self):
        asyncio.run(self.consecutive_sleeps())
        
if __name__ == "__main__":
    durations = [i for i in range(1, 11)]
    processes = [MultiprocessingAsync(durations[i*5: (i+1)*5]) for i in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
