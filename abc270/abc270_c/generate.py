#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 1000)  # TODO: edit here
    U = [None for _ in range(N - 1)]
    V = [None for _ in range(N - 1)]
    X = random.randint(1, 10 ** 9)  # TODO: edit here
    Y = random.randint(1, 10 ** 9)  # TODO: edit here
    for i in range(N - 1):
        U[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        V[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    print(N, X, Y)
    for i in range(N - 1):
        print(U[i], V[i])

if __name__ == "__main__":
    main()
