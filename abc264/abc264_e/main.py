#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, E: int, U: List[int], V: List[int], Q: int, X: List[int]) -> List[str]:
def solve(N, M, E, U, V, Q, X):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, E = map(int, input().split())
    U = [None for _ in range(E)]
    V = [None for _ in range(E)]
    for i in range(E):
        U[i], V[i] = map(int, input().split())
    Q = int(input())
    X = [None for _ in range(Q)]
    for i in range(Q):
        X[i] = int(input())
    a = solve(N, M, E, U, V, Q, X)
    for i in range(Q):
        print(a[i])

if __name__ == '__main__':
    main()
