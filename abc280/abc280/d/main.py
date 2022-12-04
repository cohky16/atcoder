# 素因数分解を行います
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

# 入力
K = int(input())

# Kの素因数を列挙します
factors = prime_factorize(K)

print(factors)

# Nを1から順に増やしながら試します
N = 1
for factor in factors:
    # N!がKの倍数となるような最小のNを求めます
    while factor ** N <= K:
        N += 1

# 答え
print(N)
