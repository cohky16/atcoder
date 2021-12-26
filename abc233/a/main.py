x,y = map(int, input().split())
print(-(-(y-x)//10) if -(-(y-x)//10) >= 0 else 0)