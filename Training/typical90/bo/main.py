n,k = map(int, input().split()) 
if n == 0: print(0)
else:
    num = str(n)
    while k > 0:
        # base 8 to 10
        t = int(num, 8)
        # base 10 to 9
        tt = ""
        while t > 0:
            tt = str(t % 9) + tt
            t //= 9
        # 8 to 5
        num = tt.replace('8', '5')
        k -= 1
    print(num)