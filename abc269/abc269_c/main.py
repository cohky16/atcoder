#!/usr/bin/env python3
# from typing import *

# def solve(X: int) -> Any:
def solve(N):
    # Nの1になるビット数を配列にする
    # 1011 -> [0,1,3]
    a = []
    for i in range(60):
        # 1011 & 1 = true -> 1011 & 10 = true -> 1011 & 100 = false
        if (N & (1 << i)):
            a.append(i)
    size = len(a)
    # 1になる桁のみでbit全探索
    # 000 -> 111 = 0 -> 7 = 0 -> 2**k-1
    for i in range(1 << size):
        cur = 0
        for j in range(size):
            # iのjビット目が1の場合
            if i & (1 << j):
                # Aのjビット目を立てる
                # 000 | 001 -> cur: 001(1), 001 | 011 -> cur: 011(3)
                cur |= (1 << a[j])
        print(cur)
    # あくまで1に着目して、1がたっているものをまとめてから、ビット全探索で数分探索して数値を作る
    # つまり、1が立っているもののビット上の組み合わせを列挙できる

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    solve(N)

if __name__ == '__main__':
    main()
