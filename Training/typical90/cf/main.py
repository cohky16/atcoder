n = int(input())
s = input()
l = []
c = 0
# ランレングス圧縮
for i in range(n):
    c += 1
    if i < n-1 and s[i] != s[i+1]:
        l.append(c)
        c = 0
l.append(c)
t = 0
# グループ間の組み合わせ数
for i in range(len(l)):
    t += l[i]*(l[i]+1)//2
print(n*(n+1)//2 - t)