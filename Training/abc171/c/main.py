n = int(input())
res = ''
while(0<n):
    n-=1
    t = n%26
    res += chr(97+t)
    n//=26
print(res[::-1])