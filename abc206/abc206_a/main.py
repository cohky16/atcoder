#!/usr/bin/env python3
# from typing import *



# def solve(N: int) -> str:
def solve(N):
    pass  # TODO: edit here
    a=int(N*1.08)
    b=206
    if a < b: return "Yay!"
    if a == b: return "so-so"
    if a > b: return ":("

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    a = solve(N)
    print(a)

if __name__ == '__main__':
    main()
