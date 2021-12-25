n = int(input())
ablist = [list(map(int,input().split())) for _ in range(n)]
ablists = sorted(ablist, key=lambda x: x[1])
t = 0
ans = "Yes"
for i in range(n):
    t += ablists[i][0]
    if t > ablists[i][1]: ans = "No" 
print(ans)
