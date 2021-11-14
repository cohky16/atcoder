n = int(input())
ans = 0
for a in range(1, int(n ** (1 / 3)) + 10): # (A * A * A <= ABC <= N) = (A <= N ** 1 / 3)
    for b in range(a, int((n / a) ** 0.5) + 10): # (ABC <= N) = (BC <= N / A) = (B * B <= BC <= N / A) = (B <= (N / A) ** 1 / 2)
        ans += max(0, int(n // (a * b)) - b + 1) # (C <= N / AB) bが開始位置なのでbを引いて+1する、負数は入れない
print(ans)

