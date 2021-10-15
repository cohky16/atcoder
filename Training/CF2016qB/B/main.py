n, a, b = map(int, input().split())
s = input()
t, r = 0, 0
for c in s:
    if c == "a" and t < a + b:
        print("Yes")
        t += 1
    elif c == "b" and t < a + b and r < b:
        print("Yes")
        t += 1
        r += 1
    else:
        print("No")