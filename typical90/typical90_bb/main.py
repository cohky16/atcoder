#!/usr/bin/env python3
# from typing import *



# def solve(a: int, b: int, c: List[int], d: List[List[int]]) -> Tuple[str, List[str]]:
def solve(a, b, c, d):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    a = int(next(tokens))
    b = int(next(tokens))
    c = [None for _ in range(b)]
    d = [[None for _ in range(c_i)] for _ in range(b)]
    for i in range(b):
        c[i] = int(next(tokens))
        for j in range(c_i):
            d[i][j] = int(next(tokens))
    assert next(tokens, None) is None
    f, h = solve(a, b, c, d)
    print(f)
    for i in range(a):
        print(h[i])

if __name__ == '__main__':
    main()
