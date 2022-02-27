n = int(input())
slist = [input() for _ in range(n)]
ans = "No"
for i in range(n):
    for j in range(n):
        if ((i+5)<n):
            # 縦
            cnt = sum([1 for k in range(6) if slist[i+k][j] == "#"])
            if cnt >= 4: ans = "Yes"
        if ((j+5)<n):
            # 横
            cnt = sum([1 for k in range(6) if slist[i][j+k] == "#"])
            if cnt >= 4: ans = "Yes"
        if ((i+5)<n and (j+5)<n):
            # 左上から斜め
            cnt = sum([1 for k in range(6) if slist[i+k][j+k] == "#"])
            if cnt >= 4: ans = "Yes"
        if ((i-5)>=0 and (j+5)<n):
            # 左下から斜め
            cnt = sum([1 for k in range(6) if slist[i-k][j+k] == "#"])
            if cnt >= 4: ans = "Yes"
print(ans)