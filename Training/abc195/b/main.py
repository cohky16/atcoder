a,b,w = map(int, input().split())
w = w*1000
bb=-(-w//b)
aa=(w//a)
if bb <= aa:
    print(bb, aa)
else:
    print('UNSATISFIABLE')