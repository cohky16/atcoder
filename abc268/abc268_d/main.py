#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, S: List[str], T: List[str]) -> str:
def solve(N, M, S, T):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    S = [None for _ in range(N)]
    T = [None for _ in range(M)]
    for i in range(N):
        S[i] = input()
    for i in range(M):
        T[i] = input()
    a = solve(N, M, S, T)
    print(a)

if __name__ == '__main__':
    main()
