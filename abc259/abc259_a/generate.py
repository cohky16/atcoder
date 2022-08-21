#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 10 ** 9)  # TODO: edit here
    M = random.randint(1, 10 ** 9)  # TODO: edit here
    X = random.randint(1, 10 ** 9)  # TODO: edit here
    T = random.randint(1, 10 ** 9)  # TODO: edit here
    D = random.randint(1, 10 ** 9)  # TODO: edit here
    print(N, M, X, T, D)

if __name__ == "__main__":
    main()
