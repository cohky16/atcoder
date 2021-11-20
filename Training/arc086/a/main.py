import collections
n, k =map(int, input().split())
l = list(map(int, input().split()))
print(sum([ v[1] for v in collections.Counter(l).most_common()[k:]]))