from decimal import ROUND_HALF_UP, Decimal


x,k = map(int, input().split())
for i in range(k+1):
    stri = '1E'+str(i)
    x = int(Decimal(x).quantize(Decimal(stri), rounding=ROUND_HALF_UP))
print(x)