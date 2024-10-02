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


def solve(n, q, x, queries):
    f = defaultdict(int)
    for i in range(1, n + 1):
        k_p = (i - 1) * (n - i + 1) + (n - i)
        f[k_p] += 1
        if i < n:
            delta = x[i] - x[i - 1] - 1
            if delta > 0:
                b = i * (n - i)
                f[b] += delta
    
    # Prepare answers for queries
    answers = [f[a] for a in queries]
    return answers
 
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, q = map(int, input().split())
        x = list(map(int, input().split()))
        queries = list(map(int, input().split()))
        result = solve(n, q, x, queries)
        results.append(result)
    
    for i in results:
        print(*i)
 
if __name__ == "__main__":
    main()
