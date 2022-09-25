#!/usr/bin/env python3
# from typing import *
import math



# def solve(a: int, b: int, d: int) -> Tuple[float, float]:
def solve(a, b, d):
    r = math.radians(d)
    x = a * math.cos(r) - b * math.sin(r)
    y = a * math.sin(r) + b * math.cos(r)
    return x, y
    

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    a, b, d = map(int, input().split())
    f, g = solve(a, b, d)
    print(f, g)

if __name__ == '__main__':
    main()