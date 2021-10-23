n = int(input())
l = list(map(int, input().split()))
a = [l[0]]
for i in range(1, n - 1):
    a.append(min(l[i - 1], l[i]))
a.append(l[-1])
print(sum(a))