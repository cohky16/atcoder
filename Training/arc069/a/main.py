n,m = map(int, input().split())
if m//2 <= n:
    print(m//2)
else:
    ans = n
    ans += (m-2*n)//4 
    print(ans)