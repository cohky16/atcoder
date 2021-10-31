s = input()
k = int(input())
r = "1"
if k <= len(s):
    for i in range(k):
        if s[i] != "1" and r == "1": r = s[i]
    print(r)
else:
    for i in s:
        if s != "1" and r == "1": r = i
    print(r)