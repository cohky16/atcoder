from decimal import Decimal
a,b,c = input().split()
ad = Decimal(a).sqrt()
bd = Decimal(b).sqrt()
cd = Decimal(c).sqrt()
print("Yes" if ad + bd < cd else "No")