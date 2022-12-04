# H, W は、それぞれマス目の行数と列数
H, W = map(int, input().split())

# S は、H 行 W 列のマス目
S = [input() for _ in range(H)]

# cnt は、マス目上の '#' の個数
cnt = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            cnt += 1

# cnt を出力する
print(cnt)