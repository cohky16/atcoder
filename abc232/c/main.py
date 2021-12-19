import itertools
n,m = map(int, input().split())
a = [[False]*n for _ in range(n)] 
b = [[False]*n for _ in range(n)]

for _ in range(m): # ボールを結ぶ紐が存在するか(高橋くん)
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    a[u][v] = a[v][u] = True # 無向グラフ
for _ in range(m): # ボールを結ぶ紐が存在するか(青木くん)
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    b[u][v] = b[v][u] = True # 無向グラフ

ans = False
for p in itertools.permutations(range(n)): # 制約が緩いため、順列全探索
    ok = True
    for i in range(n):
        for j in range(n):
            if a[i][j] != b[p[i]][p[j]]:
                ok = False
    if ok:
        ans = True
print("Yes" if ans else "No")