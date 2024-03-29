#!/usr/bin/env python3
# from typing import *

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
from collections import deque

def main():
    N, X, Y = map(int, input().split()); X-=1; Y-=1
    # グラフ作成
    G=[[] for _ in range(N)]
    for _ in range(N-1):
        u,v = map(int, input().split()); u-=1; v-=1
        G[u].append(v); G[v].append(u)
    # 両端キュー
    D=deque(); D.append(X)
    # 到達済みリスト
    seen=[0]*N; seen[X]=1
    # メモ
    rec = {}
    # DFS
    while D:
        now=D.popleft()
        for nxt in G[now]:
            # 到達済みなら次に
            if seen[nxt]:
                continue
            seen[nxt]=1
            rec.setdefault(nxt, now)
            D.append(nxt)
    ans=[]
    n=Y
    # X -> Yまで復元
    while n != X:
        ans.append(n+1)
        n=rec[n]
    ans.append(n+1)
    print(*reversed(ans), sep=" ")

if __name__ == '__main__':
    main()
