v,a,b,c = map(int, input().split())
l=[a,b,c]
s="FMT"
c=0
while v > 0: 
    v-=l[c]
    if v < 0: break
    c += 1
    if c == 3: c = 0
print(s[c])