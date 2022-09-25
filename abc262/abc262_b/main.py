#!/usr/bin/env python3
# from typing import *
from collections import defaultdict


# def solve(N: int, M: int, U: List[int], V: List[int]) -> int:
def solve(N, M, G):
    ans = 0
    for a in range(1, N-1):
        for b in range(a+1, N):
            for c in range(b+1, N+1):
                if b in G[a] and c in G[b] and a in G[c]:
                    ans += 1
    return ans



# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    G = defaultdict(list)
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    a = solve(N, M, G)
    print(a)

if __name__ == '__main__':
    main()