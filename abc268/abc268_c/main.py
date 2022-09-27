#!/usr/bin/env python3
# from typing import *



# def solve(N: int, p: List[int]) -> int:
from itertools import accumulate


def solve(N, p):
    cum = [0]*N
    # すべての人を探索
    for i in range(N):
        # 料理p[i]は人p[i-1],[i],[i+1]にあると人p[i]が喜ぶ
        cum[(N-p[i]+i-1)%N] += 1
        cum[(N-p[i]+i)%N] += 1
        cum[(N-p[i]+i+1)%N] += 1
    return max(cum)

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    p = [None for _ in range(N)]
    for i in range(N):
        p[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, p)
    print(a)

if __name__ == '__main__':
    main()
