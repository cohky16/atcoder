#!/usr/bin/env python3
# from typing import *

MOD = 1000000007

# def solve(N: int, c: List[str], a: List[int], b: List[int]) -> int:
def solve(N, c, a, b):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    c = [None for _ in range(N)]
    a = [None for _ in range(N - 1)]
    b = [None for _ in range(N - 1)]
    for i in range(N):
        c[i] = next(tokens)
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    assert next(tokens, None) is None
    a1 = solve(N, c, a, b)
    print(a1)

if __name__ == '__main__':
    main()
