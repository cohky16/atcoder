n=int(input())
l=list(map(int,input().split()))[::-1]
r = "Yes"
for i, a in enumerate(l):
    if i != 0:
        if l[i - 1] < l[i]: l[i] -= 1
        if l[i - 1] < l[i]: r = "No"
print(r)
