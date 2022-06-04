from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    A.append(A[i])

B=[0]*len(A)
B[0] = A[0]
for i in range(len(A)-1):
    B[i+1] = B[i] + A[i+1]

if B[N-1] % 10 != 0: exit(print("No"))

# 目標値
num = B[N-1]//10

for i in range(N):
    j = bisect_left(B, num + B[i])
    if B[j] - B[i] == num: 
        exit(print("Yes"))
print("No")