﻿


__version__ = "0.2019.10.19"



import concurrent.futures
import asyncio




executor = concurrent.futures.ThreadPoolExecutor(max_workers=32)



async def call_sync(synchroneousCallable, *args, **kwargs):
	assert callable(synchroneousCallable)

	loop = asyncio.get_event_loop()
	result = await loop.run_in_executor(executor, synchroneousCallable, *args, **kwargs)
	return result
#





def make_async(synchroneousCallable):
	assert callable(synchroneousCallable)

	async def func_wrapper(*args, **kwargs):
		loop = asyncio.get_event_loop()
		result = await loop.run_in_executor(executor, synchroneousCallable, *args, **kwargs)
		return result
	#

	return func_wrapper
#

