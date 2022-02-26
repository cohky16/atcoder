n = int(input())
slist = [input() for _ in range(n)]
ans = "No"
for i in range(n):
    for j in range(n-6):
        if slist[i][j:j+6].count("#") >= 4: ans = "Yes"
for i in range(n):
    for j in range(n):
        if slist[j][i:i+6].count("#") >= 4: ans = "Yes"
for i in range(n-5):
    for j in range(n-5-i):
        d = ""
        u = ""
        for k in range(6):
            d += slist[i+j+k][j+k]
            u += slist[j+k][i+j+k]
        if d.count("#") >= 4: ans = "Yes"
        if u.count("#") >= 4: ans = "Yes"
for i in range(n-1, n-6,-1):
    for j in range(i-4):
        d = ""
        u = ""
        for k in range(6):
            d += slist[i-j-k][j+k]
            u += slist[j+k][i-j-k]
        if d.count("#") >= 4: ans = "Yes"
        if u.count("#") >= 4: ans = "Yes"
print(ans)