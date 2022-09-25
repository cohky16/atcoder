#!/usr/bin/env python3
# from typing import *



# def solve(N: int, X: int, Y: int, Z: int, A: List[int], B: List[int]) -> Tuple[List[str], List[str], str]:
def solve(N, X, Y, Z, A, B):
    ans = []
    a = sorted(A, reverse=True)
    for i in range(X):
        aa = A.index(a[i])
        ans.append(aa+1)
        A[aa] = -1
        B[aa] = -1
    b = sorted(B, reverse=True)
    for i in range(Y):
        bb = B.index(b[i])
        ans.append(bb+1)
        A[bb] = -1
        B[bb] = -1
    C = [A[i] + B[i] for i in range(N)]
    c = sorted(C, reverse=True)
    for i in range(Z):
        if c[i] >= 0:
            cc = C.index(c[i])
            ans.append(cc+1)
            C[cc] = -1
    for aaa in sorted(ans):
        print(aaa)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = int(next(tokens))
    Y = int(next(tokens))
    Z = int(next(tokens))
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    for i in range(N):
        B[i] = int(next(tokens))
    assert next(tokens, None) is None
    solve(N, X, Y, Z, A, B)

if __name__ == '__main__':
    main()