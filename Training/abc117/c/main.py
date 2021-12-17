n,m = map(int, input().split())
xlist = list(map(int, input().split()))
if n >= m: print(0)
else:
    xlist.sort()
    xxlist = [abs(xlist[i - 1] - xlist[i]) for i in range(1, m)]
    xxlist.sort()
    print(sum(xxlist[:m-n]))
        
