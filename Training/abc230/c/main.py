n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
k1 = [max(1-a,1-b), min(n-a,n-b)]
k2 = [max(1-a,b-n), min(n-a,b-1)]
for i in range(p, q + 1):
    ans = ""
    for j in range(r, s + 1):
        if k1[0] <= i - a <= k1[1] and b + (i - a) == j:
            ans += "#"
        elif k2[0] <= i - a <= k2[1] and b - (i - a) == j:
            ans += "#"
        else:
            ans += "."
    print(ans)