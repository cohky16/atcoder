n = int(input())
d, x = map(int, input().split())
r = x
for i in range(n):
    t = int(input())
    r += -(-d // t)
print(r)