import queue
n = int(input())
abj = [[] for _ in range(n + 1)]
depth = [-1] * (n + 1) # 深さのリスト
for i in range(1, n + 1):
    vlist = list(map(int, input().split()))
    for v in vlist[2:]:
        abj[i].append(v)
q = queue.Queue()
q.put((1,0))
while not q.empty():
    x, d = q.get()
    if depth[x] != -1: # 探索済みの場合、次へ
        continue
    depth[x] = d
    for next in abj[x]: # queから取りだしたものの次
        if depth[next] == -1:
            q.put((next, d + 1))
for i in range(1, n + 1):
    print(i, depth[i])

