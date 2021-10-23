a, b = map(int, input().split())
r = 0
for i in range(a, b + 1):
    s = str(i)
    if s == ''.join(reversed(list(s))): r += 1
print(r)