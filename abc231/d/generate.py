#!/usr/bin/env python3
import random
N = random.randint(2, 10**5)
M = random.randint(0, 10**5)
print(N, M)
for _ in range(M):
    a = random.randint(1, N - 1)
    b = random.randint(a + 1, N)
    print(a, b)
