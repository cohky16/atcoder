#!/usr/bin/env python3
# from typing import *



# def solve(W: int, N: int, L: List[int], R: List[int]) -> List[str]:
def solve(W, N, L, R):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    W, N = map(int, input().split())
    L = [None for _ in range(N)]
    R = [None for _ in range(N)]
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    ans = solve(W, N, L, R)
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()
