n,x = map(int, input().split())
ans = list(map(int, input().split()))[1:]
for i in range(1,n):
    t = list(map(int, input().split()))[1:]
    tt = []
    for j in range(len(ans)):
        for k in range(len(t)):
            tt.append(ans[j] * t[k])
    ans = tt
print(sum([1 for a in ans if a == x]))


