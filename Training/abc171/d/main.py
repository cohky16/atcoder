from collections import Counter


n = int(input())
alist = list(map(int, input().split()))
q = int(input())
cnt = Counter(alist)
ans = sum(alist)
for i in range(q):
    b,c = map(int, input().split())
    if b in cnt:
        ans = ans-(b*cnt[b])+(c*cnt[b])
        cnt[c] += cnt[b]
        cnt[b] = 0
    print(ans)

