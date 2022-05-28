from itertools import count


n = int(input())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
clist = list(map(int, input().split()))
acount = [0 for _ in range(46)]
bcount = [0 for _ in range(46)]
ccount = [0 for _ in range(46)]
for i in range(n):
    acount[alist[i]%46] += 1
    bcount[blist[i]%46] += 1
    ccount[clist[i]%46] += 1
ans = 0
for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a + b + c) % 46 == 0:
                ans += acount[a] * bcount[b] * ccount[c]
print(ans)