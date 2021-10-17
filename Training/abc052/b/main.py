n = int(input())
s = input()
x, r = 0, 0
for c in s:
    if c == "I": x += 1
    else: x -= 1
    r = max(r, x)
print(r)