from functools import lru_cache
from typing import Generator

calls = 0

# Naive recursion
def fib1(n: int) -> int:
    global calls 
    calls += 1
    if n < 2:
        return n
    return fib1(n - 2) + fib1(n - 1)

# With memoization
memo = { 0: 0, 1: 1 }

def fib2(n: int) -> int:
    global calls 
    calls += 1
    if n not in memo:
        memo[n] = fib2(n - 2) + fib2(n - 1)
    return memo[n]

# Memoization with functools
@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    global calls 
    calls += 1
    if n < 2:
        return n
    return fib3(n - 2) + fib3(n - 1)

# Iterating with tuple unpacking -> 2 less calls
def fib4(n: int) -> int:
    if n == 0: return n # special case
    last = 0 # initially set to fib(0)
    next = 1 # initially set to fib(1)
    for _ in range(1, n):
        global calls 
        calls += 1
        last, next = next, last + next
    return next

# Making generator, which returns any number
def fib5(n: int) -> Generator[int, None, None]:
    yield 0 # special case
    if n > 0: yield 1 # special case
    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)
    for _ in range(1, n):
        global calls 
        calls += 1
        last, next = next, last + next
        yield next # main generation step

if __name__ == "__main__":
    print(fib4(20))
    print(calls)

    # Generator output
    for i in fib5(50):
        print(i)