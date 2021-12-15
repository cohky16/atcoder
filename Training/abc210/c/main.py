import collections
n,k = map(int, input().split())
c = list(map(int, input().split()))
counter = collections.Counter(c[:k])
ans = len(counter)
for i in range(k, n):
    left = c[i - k]
    right = c[i]
    counter[left] -= 1
    counter[right] += 1
    if counter[left] == 0:
        del counter[left]
    ans = max(ans, len(counter))
print(ans)
