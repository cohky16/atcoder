n = int(input())
slist = [[0]*n for _ in range(10)] 
for i in range(n):
    temp = list(map(int, input()))
    for j in range(10):
        slist[j][i] = temp.index(j)
ans = []
for s in slist:
    for i in range(n):
        s[i] += ((s.count(s[i])-1)*10)
    ans.append(max(s))
print(min(ans))