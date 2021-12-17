a,b,c = map(int, input().split())
l = sorted([a,b,c], reverse=True)
print(l[0] + l[1])