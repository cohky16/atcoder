n = int(input())
r = 10**12 + 1
for i in range(1, int(n**0.5) + 1):
    if n % i == 0 and (n / i).is_integer():
        r = min(r, int(i + n / i - 2))
print(r)