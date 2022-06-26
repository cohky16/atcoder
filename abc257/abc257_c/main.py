#!/usr/bin/env python3
# from typing import *


INF = pow(10, 18)

# def solve(N: int, S: str, W: List[int]) -> int:
def solve(N, S, W):
    if len(set(S)) == 1: return N
    slist = []
    cnt = 0
    # 二次元配列で値とインデックスをソートできるように保持
    for i in range(N):
        slist.append([W[i], S[i]])
        # 大人の数を数え上げておく
        if S[i] == '1': 
            cnt += 1
    slist.sort()
    ans = cnt
    for i in range(N):
        w,s = slist[i]
        # iに対して子どもがきたら合計値を増やす
        if s == '0': cnt += 1
        # iに対して大人がきたら合計値を減らす
        if s == '1': cnt -= 1
        # リストの最後か次が繰り返しではない場合に値を更新する
        if i+1 == N or slist[i+1][0] != w:
            ans = max(ans, cnt)
    return (ans)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    W = [None for _ in range(N)]
    S = next(tokens)
    for i in range(N):
        W[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, S, W)
    print(a)

if __name__ == '__main__':
    main()
