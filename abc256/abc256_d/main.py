#!/usr/bin/env python3
# from typing import *



# def solve(N: int, L: List[int], R: List[int]) -> Tuple[List[str], List[str]]:
from bisect import bisect, bisect_left


def solve(N, L, R):
    pass  # TODO: edit here
    ans = {L[0], R[0]}
    for i in range(1, N):
        o = ans | {L[i], R[i]}
        if ans & {L[i], R[i]}:
            ans = {min(o),max(o)}
        else:
            ans = ans.union(o)
    for iKs in sorted(ans):
        


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    L = [None for _ in range(N)]
    R = [None for _ in range(N)]
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    solve(N, L, R)

if __name__ == '__main__':
    main()
