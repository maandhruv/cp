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

# input = sys.stdin.read 
# sys.setrecursionlimit(10**6)

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
def count_overlaps(start, d, jobs):
    end = start + d - 1
    return sum(1 for l, r in jobs if not (end < l or start > r))


def solve():
    n, dur, jobs_count = map(int, input().split())
    stdays = {}
    endways = {}
    
    for _ in range(jobs_count):
        st, en = map(int, input().split())
        stdays[st] = stdays.get(st, 0) + 1
        endways[en] = endways.get(en, 0) + 1
    
    minover, maxover = 0, 0
    mn, mx = 1, 1
    countover = 0
    
    for day in range(1, dur + 1):
        if day in stdays:
            countover += stdays[day]
    
    minover = maxover = countover

    for day in range(2, n - dur + 2):
        if day + dur - 1 in stdays:
            countover += stdays[day + dur - 1]
        if day - 1 in endways:
            countover -= endways[day - 1]
        if countover > maxover:
            maxover = countover
            mx = day
        if countover < minover:
            minover = countover
            mn = day

    print(mx, mn)


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        solve()


if __name__ == "__main__":
    main()
