#Жрёт кучу памяти
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)
#print(fib(6))

#Случай с мемоизацией
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}

def fib_memo(n:int) -> int:
    if n not in memo:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

#print(fib_memo(6))

#Случай с декоратором

from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cache(n:int) -> int:
    if n < 2:
        return n
    return fib_cache(n-2) + fib_cache(n-1)
#print(fib_cache(6))


#Случай с итерациями

def fib_iter(n:int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
    return next
#print(fib_iter(6))

#Случай с генератором

from typing import Generator

def fib_gen(n:int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

for i in fib_gen(50):
    print(i)
