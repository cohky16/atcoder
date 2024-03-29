#!/usr/bin/env python3
# from typing import *



# def solve(N: int, X: int, Y: int) -> int:
def solve(N, X, Y):
    r,b = [0]*12, [0]*12
    b[1] = 1
    for i in range(2, N+1):
        b[i] = r[i-1] + b[i-1]*Y
        r[i] = r[i-1] + b[i]*X
    return r[N]

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, X, Y = map(int, input().split())
    a = solve(N, X, Y)
    print(a)

if __name__ == '__main__':
    main()
