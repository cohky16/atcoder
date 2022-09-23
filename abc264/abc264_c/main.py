#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    h,w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    h2,w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]
    ans = False
    for i in range(1 << h):
        bb = []
        for ii in range(h):
            if i & 1 << ii: bb.append(a[ii])
        for j in range(1 << w):
            cc = [[] for _ in range(len(bb))]
            for jj in range(w):
                if j & 1 << jj:
                    for i,v in enumerate(bb):
                        cc[i].append(v[jj])
            if b == cc: 
                ans = True
    print(YES if ans else NO)


if __name__ == '__main__':
    main()
