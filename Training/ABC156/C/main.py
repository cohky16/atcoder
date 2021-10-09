n = int(input())
l = list(map(int, input().split()))
r = 1000000

for i in range(100):
    r = min(r, sum([(p - i) ** 2 for p in l]))
print(r)