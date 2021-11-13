l = [list(map(int, input().split())) for i in range(3)]
num = 0
for i in range(3):
    aaa = min(l[i])
    l[i][0] -= aaa
    l[i][1] -= aaa
    l[i][2] -= aaa
    bbb = max(l[i])
    l[i][0] -= bbb
    l[i][1] -= bbb
    l[i][2] -= bbb
print("Yes") if l[0] == l[1] == l[2] else print("No")