import sys
import math
import bisect
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, combinations
from functools import lru_cache
import os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("error.txt", "w")

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

    n = inp()
    arr = inlt()
    if n<=2:
        print(max(arr) + 1)
        return
    even = []
    odd = []
    for i in range(0,n,2):
        even.append(arr[i])
    for i in range(1,n,2):
        odd.append(arr[i])

    es = len(even) + max(even)
    ds = len(odd) + max(odd)

    es = len(even) + (max(even) if even else max(arr))
    ds = len(odd) + (max(odd) if odd else max(arr))

    print(max(es, ds))

def main():

    t = inp()  # Number of test cases
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()



    
