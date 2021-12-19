n = int(input())
adj = [[] for _ in range(n)] # 隣接する要素番号を入れる
for i in range(n):
    vlist = list(map(int, input().split()))
    for v in vlist[2:]:
        adj[i].append(v-1)
d = [0]*n # 発見時刻のリスト
f = [0]*n # 完了時刻のリスト

def dfs(i,t):
    t += 1
    d[i] = t # 発見時刻
    for next in adj[i]:
        if d[next] == 0:
            t = dfs(next, t) # nextを再帰で探索して完了時刻を返す
    t += 1
    f[i] = t # 探索が全て終わったら完了時刻を入れる
    return t

t = 0
for i in range(n):
    if d[i] == 0:
        t = dfs(i, t)
    print(i + 1, d[i], f[i])