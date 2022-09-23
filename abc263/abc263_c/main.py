#!/usr/bin/env python3
# from typing import *
from itertools import permutations


# def solve(N: int, M: int) -> Tuple[List[str], List[List[str]], List[List[str]], List[List[List[str]]]]:
def solve(N, M):
    for per in permutations(range(1, M+1), N):
        f = True
        b = 0
        for i in range(N):
            if b < per[i]: 
                b = per[i]
            else: 
                f = False
                break
        if f:
            print(*per)

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    solve(N, M)

if __name__ == '__main__':
    main()
