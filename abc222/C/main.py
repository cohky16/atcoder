# TODO
def check(a, b):
    if a == b: return 0
    if a == "G" and b == "C": return 1
    if a == "C" and b == "G": return -1
    if a == "C" and b == "P": return 1
    if a == "P" and b == "C": return -1
    if a == "P" and b == "G": return 1
    if a == "G" and b == "P": return -1
n, m = map(int, input().split())
A = [input() for i in range(n * 2)]
r = [0]*(n*2)
for i in range(m):
    for j in range(0, n * 2, 2):a
        r[j] += check(A[j][i], A[j + 1][i])
print(r)

