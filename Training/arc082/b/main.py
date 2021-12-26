n = int(input())
plist = list(map(int, input().split()))
ans = 0
i = 0
while i < n:
    if plist[i] == i + 1:
        ans += 1
        i += 2
    else:
        i += 1
print(ans)