#!/usr/bin/env python3
# from typing import *



# def solve(N: int, L: List[int], R: List[int]) -> float:
def solve(N, L, R):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    L = [None for _ in range(N)]
    R = [None for _ in range(N)]
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    a = solve(N, L, R)
    print(a)

if __name__ == '__main__':
    main()
