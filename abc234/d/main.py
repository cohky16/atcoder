import heapq
n,k = map(int, input().split())
plist = list(map(int, input().split()))
que = plist[:k] # 0~kのリスト
print(min(que))
heapq.heapify(que) # ヒープ(優先度付きキュー)に変換
for i in range(k,n):
    minima=heapq.heappop(que) # 最小値を取り出す
    minima=max(minima,plist[i]) # 検索対象と最小値の大小
    heapq.heappush(que,minima) # 要素を挿入
    ans = heapq.heappop(que) # 最小値を取り出す
    print(ans)
    heapq.heappush(que,ans) # 要素を挿入
