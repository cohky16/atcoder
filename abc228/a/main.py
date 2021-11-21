s, t, x = map(int, input().split())
if s < t and s <= x < t: print("Yes") 
elif s > t:
    if s > t > x and s <= x + 24 < t + 24:  print("Yes") 
    elif s > t < x and s <= x < t + 24: print("Yes")
    else: print("No")
else: print("No")