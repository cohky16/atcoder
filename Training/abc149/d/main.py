n,k = map(int, input().split())
r,s,p = map(int, input().split())
tlist = list(input())
before = ""
ans = 0
for i in range(n):
    if tlist[i] == "r": 
        if i >= k and tlist[i - k] == "r" and before[i - k] == "p": 
            before += "r"
            continue
        ans += p
        before += "p"
    if tlist[i] == "s": 
        if i >= k and tlist[i - k] == "s" and before[i - k] == "r": 
            before += "s"
            continue
        ans += r
        before += "r"
    if tlist[i] == "p":
        if i >= k and tlist[i - k] == "p" and before[i - k] == "s": 
            before += "p"
            continue
        ans += s
        before += "s"
print(ans)