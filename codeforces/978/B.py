import sys
import math
import bisect
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, combinations
from functools import lru_cache
import os

input = sys.stdin.read 
sys.setrecursionlimit(10**6)

def inp():
    return int(sys.stdin.readline().strip())

def inlt():
    return list(map(int, sys.stdin.readline().strip().split()))

def insr():
    """Reads a string as a list of characters."""
    return list(sys.stdin.readline().strip())

def invr():
    return tuple(map(int, sys.stdin.readline().strip().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]

def binary_search(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def lower_bound(arr, target):
    """Finds the first position where target can be inserted without breaking order."""
    return bisect.bisect_left(arr, target)

def upper_bound(arr, target):
    """Finds the first position where target is strictly greater than the target."""
    return bisect.bisect_right(arr, target)

def sort_by_second(elem):
    """Sorts a list of tuples by the second element."""
    return sorted(elem, key=lambda x: x[1])

def solve():

    n, x = inlt()
    arr = inlt()
    h = []
    for i in range(n):
        heappush(h, -arr[i])
    buy = 0
    ans = 0
    while buy < sum(arr):
        l = []
        for i in range(x):
            a = -heappop(h) if h else 0
            if a == 0:
                break
            buy += 1
            if a > 1:
                l.append(a - 1)
        for i in range(len(l)):
            heappush(h, -l[i])
        ans += 1
    print(ans)

def solve1():

    n, x = inlt()
    arr = inlt()
    mx = max(arr)
    s = sum(arr)
    a = (s + x - 1) // x
    ans = max(mx, a)
    print(ans)
    
def main():

    t = inp()  # Number of test cases
    for _ in range(t):
        solve1()


if __name__ == "__main__":
    main()



    
