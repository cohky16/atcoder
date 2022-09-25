#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'

# def solve(S: str, T: str) -> str:
def solve(S, T):
    if len(S) > len(T) or S[0] != T[0] or S[-1] != T[-1]: return NO
    l = []
    p = ""
    for c in list(S):
        if p == c: l[-1] += 1
        else: l.append(1)
        p = c
    ll = []
    p = ""
    for c in list(T):
        if p == c: ll[-1] += 1
        else: ll.append(1)
        p = c
    if len(l) != len(ll): return NO
    ss = 0
    tt = 0
    for s,t in zip(l, ll):
        ss += s
        tt += t
        if s > t or (s == 1 and t > s) or S[ss-1] != T[tt-1]: return NO
    return YES

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    T = input()
    a = solve(S, T)
    print(a)

if __name__ == '__main__':
    main()