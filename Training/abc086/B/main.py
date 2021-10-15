a, b = input().split()
n = int(a + b)
print("Yes" if (n**0.5).is_integer() else "No")
