w,h,x,y = map(int, input().split())
ans1 = w*h / 2
ans2 = 1 if x*2==w and y*2==h else 0
print(ans1, ans2)