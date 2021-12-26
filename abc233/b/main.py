l,r = map(int, input().split())
s = list(input())
print("".join(s[:l-1]) + "".join(list(reversed(s[l-1:r]))) + "".join(s[r:]))