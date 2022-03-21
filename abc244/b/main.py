n = int(input())
t = input()
ans = [0,0]
row = ["W","S","E","N"]
now = 0
for i in range(n):
    if t[i] == "S":
        if row[now] == "W": ans[0] += 1
        if row[now] == "S": ans[1] -= 1
        if row[now] == "E": ans[0] -= 1
        if row[now] == "N": ans[1] += 1
    else:
        now += 1
        now %= 4
print(ans[0], ans[1])