#!/usr/bin/env python3
# from typing import *



# def solve(N: int, C: int, T: List[int], A: List[int]) -> List[str]:
def solve(N, C, T, A):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, C = map(int, input().split())
    T = [None for _ in range(N)]
    A = [None for _ in range(N)]
    for i in range(N):
        T[i], A[i] = map(int, input().split())
    ans = solve(N, C, T, A)
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()
