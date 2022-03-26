import datetime
a,b,c,d = map(int, input().split())
print("Takahashi" if datetime.datetime(2020,10,10, a,b) < datetime.datetime(2020,10,10, c,d, 1) else "Aoki")