n = int(input())
s,t = [], []
# 姓と名のリスト
for i in range(n):
    u,v = input().split()
    s.append(u)
    t.append(v)
# 全探索
for i in range(n):
    f = False
    # 自分の姓と名
    for S in [s[i], t[i]]:
        ff = True
        # 自分以外で姓か名が一致していたらfalse
        for j in range(n):
            if i != j:
                if S == s[j] or S == t[j]:
                    ff = False
        if ff:
            f = True
    if not f:
        print("No")
        exit()
print("Yes")