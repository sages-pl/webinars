from time import time
from mylib import fib

start = time()
fib(32)
end = time()

duration = end - start
print(f'Duration: {duration:.3f}')
