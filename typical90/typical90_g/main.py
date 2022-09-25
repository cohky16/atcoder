#!/usr/bin/env python3
# from typing import *

from bisect import bisect


MOD = 998244353

# def solve(N: int, A: List[int], Q: int, B: List[int]) -> List[str]:
def solve(N, A, Q):
    A.sort()
    for i in range(Q):
        b = int(input())
        t = bisect(A, b)
        if t == 0: print(abs(A[t]-b))
        elif t == len(A): print(abs(A[t-1]-b))
        else: print(min(abs(A[t]-b), abs(A[t-1]-b)))

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    solve(N, A, Q)

if __name__ == '__main__':
    main()