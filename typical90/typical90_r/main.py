#!/usr/bin/env python3
# from typing import *



# def solve(T: int, L: int, X: int, Y: int, Q: int, E: List[int]) -> List[str]:
def solve(T, L, X, Y, Q, E):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    E = [None for _ in range(Q)]
    for i in range(Q):
        E[i] = int(input())
    a = solve(T, L, X, Y, Q, E)
    for i in range(Q):
        print(a[i])

if __name__ == '__main__':
    main()
