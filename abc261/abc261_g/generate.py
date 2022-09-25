#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = ''.join([random.choice('abcde') for _ in range(random.randint(1, 100))])  # TODO: edit here
    T = ''.join([random.choice('abcde') for _ in range(random.randint(1, 100))])  # TODO: edit here
    K = random.randint(1, 1000)  # TODO: edit here
    C = [None for _ in range(K)]
    A = [None for _ in range(K)]
    for i in range(K):
        C[i] = random.choice('abcde')  # TODO: edit here
        A[i] = ''.join([random.choice('abcde') for _ in range(random.randint(1, 100))])  # TODO: edit here
    print(S)
    print(T)
    print(K)
    for i in range(K):
        print(C[i], A[i])

if __name__ == "__main__":
    main()