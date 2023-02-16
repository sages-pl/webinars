from time import time
from fastapi import FastAPI


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)


def run():
    start = time()
    factorial(500)
    factorial(700)
    factorial(500)
    factorial(800)
    factorial(900)
    factorial(950)
    end = time()
    duration = end - start

    print(f'Duration: {duration} seconds')