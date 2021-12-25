from collections import Counter
n = int(input())
alist = list(map(int, input().split()))
clist = sorted([[k,v] for k,v in Counter(alist).items() if v >= 2],reverse=True)
if len(clist) == 0: print(0)
elif clist[0][1] >= 4: print(clist[0][0] * clist[0][0])
else: print(clist[0][0] * clist[1][0])
