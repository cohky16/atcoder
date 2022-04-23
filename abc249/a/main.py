l = ["","",""]
A,B,C,D,E,F,X = map(int, input().split())
ta = 0
tans = 0
while ta <= X:
    t =  A if A + ta <= X else X-ta
    ta += (A+C)
    tans += (t*B)
tb = 0
tbans = 0
while tb <= X:
    t =  D if D + tb <= X else X-tb
    tb += (D+F)
    tbans += (t*E)
if tans == tbans: print("Draw")
elif tans > tbans: print("Takahashi")
else: print("Aoki")