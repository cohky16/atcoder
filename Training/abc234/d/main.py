import heapq

n,k = map(int, input().split())
plist = list(map(int, input().split()))
que = plist[0:k]
print(min(que))
heapq.heapify(que)
for i in range(k,n):
    mini = heapq.heappop(que)
    mini = max(mini, plist[i])
    heapq.heappush(que, mini)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)