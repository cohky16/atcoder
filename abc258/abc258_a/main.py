#!/usr/bin/env python3
# from typing import *
import datetime


# def solve(K: int) -> str:
def solve(K):
    date = datetime.datetime(2000,1,1,21,00)
    res = date + datetime.timedelta(minutes=K)
    return format(res.hour, "02d") + ':' + format(res.minute, "02d")

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    K = int(input())
    a = solve(K)
    print(a)

if __name__ == '__main__':
    main()
