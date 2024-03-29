#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, A: List[int]) -> int:
from itertools import accumulate


def solve(N, M, A):
    to = [0 for _ in range(N-M+1)]
    # 初項
    to[0] = sum([(i+1)*v for i, v in enumerate(A[:M])])
    # 累積和
    cum = [0] + list(accumulate(A))
    # 初項以降を取得
    for i in range(1, N-M+1):
        # 前の項 - (前の累積和 + 次の累積和 -> 一個前の和のみ引く) + 追加分
        to[i] = to[i-1] - cum[i+M-1] + cum[i-1] + M*A[i+M-1]
    return(max(to))


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, A)
    print(a)

if __name__ == '__main__':
    main()
