n,m = map(int, input().split())
time = 1900 * m + 100 * (n - m)
x = 2**m # 期待値はACする確率の逆数
ans = time * x
print(ans)