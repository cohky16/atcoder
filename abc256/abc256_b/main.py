#!/usr/bin/env python3
# from typing import *



# def solve(N: int, A: List[int]) -> int:
def solve(N, A):
    pass  # TODO: edit here
    l = [0, 0, 0, 0]
    p = 0
    for i in range(N):
        l[0] = 1
        for j in reversed(range(4)):
            if l[j]:
                if j + A[i] >= 4:
                    l[j] = 0
                    p += 1
                else:
                    l[j+A[i]] = l[j]
                    l[j] = 0
    return p


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A)
    print(a)

if __name__ == '__main__':
    main()
