from decimal import Decimal, ROUND_HALF_UP
x = input()
print(Decimal(x).quantize(Decimal('0'), rounding=ROUND_HALF_UP))