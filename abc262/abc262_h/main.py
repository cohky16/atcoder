#!/usr/bin/env python3
# from typing import *

MOD = 998244353

# def solve(N: int, M: int, Q: int, L: List[int], R: List[int], X: List[int]) -> int:
def solve(N, M, Q, L, R, X):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, Q = map(int, input().split())
    L = [None for _ in range(Q)]
    R = [None for _ in range(Q)]
    X = [None for _ in range(Q)]
    for i in range(Q):
        L[i], R[i], X[i] = map(int, input().split())
    a = solve(N, M, Q, L, R, X)
    print(a)

if __name__ == '__main__':
    main()
