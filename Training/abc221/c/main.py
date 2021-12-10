N = input()
L = len(N)
ans = 0
for bit in range(1 << L): # 1を桁数分ビットシフト(=2**n)
    a,b = [], []
    for i in range(L):
        if bit & (1 << i): # i桁目が1かチェック
            a.append(int(N[i]))
        else:
            b.append(int(N[i]))
    if not a or not b: continue
    a.sort(reverse=True)
    a = int("".join(map(str, a)))
    b.sort(reverse=True)
    b = int("".join(map(str, b)))
    ans = max(ans, a * b)
print(ans)
