n,k = map(int, input().split())
l=[]
# 満点との差分と部分点を足せば満点を選ぶことになる
for i in range(n):
    a,b = map(int, input().split())
    l.append(a-b)
    l.append(b)
l.sort(reverse=True)
print(sum(l[:k]))

