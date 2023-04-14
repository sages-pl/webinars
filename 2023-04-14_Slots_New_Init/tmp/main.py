from time import time
from mylib import fib


start = time()
fib(32)
stop = time()

duration = stop - start
print(f'Duration {duration:.3f} seconds')