n,a,b =map(int, input().split())
mi=(a*(n-1))+b
ma=(b*(n-1))+a
print(ma - mi + 1) if ma - mi + 1 > 0 else print(0)
