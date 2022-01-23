s = list(input())
a,b = map(int, input().split())
t = s[a - 1]
s[a - 1] = s[b - 1]
s[b - 1] = t
print("".join(s))