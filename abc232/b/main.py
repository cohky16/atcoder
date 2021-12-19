s = input()
t = input()
l = "abcdefghijklmnopqrstuvwxyz"*2
ans = "No"
for i in range(27):
    tmp = ""
    for c in s:
        tmp += l[l.index(c) + i]
    if tmp == t: 
        ans = "Yes"
print(ans)