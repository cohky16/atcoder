h,w = map(int, input().split())
ans = [[0,0], [0,0]]
f = False
for i in range(h):
    s = input()
    if s.count('o') and not f: 
        ans[0][0] = i
        ans[0][1] = s.index('o')
        f = True
    if s.count('o'):
        ans[1][0] = i
        ans[1][1] = s.rfind('o')
print(abs(ans[1][0]-ans[0][0])+abs(ans[1][1]-ans[0][1]))

