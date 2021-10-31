n = int(input())
a = list(map(int, input().split()))
r = 0
for i in a:
    r += i - 1
print(r)