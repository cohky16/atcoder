n = int(input())
a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())
A = sorted(a)
B = sorted(b)
C = sorted(c)

def binary_l(array, target):
    start = 0
    end = len(array)
    while start < end:
        mid = (end + start) // 2
        if array[mid] < target: # a < b
            start = mid + 1
        else:
            end = mid
    return start

def binary_r(array, target):
    start = 0
    end = len(array)
    while start < end:
        mid = (end + start) // 2
        if target < array[mid]: # b < c
            end = mid
        else:
            start = mid + 1
    return start

ans = 0
for bb in B:
    ac = binary_l(A, bb)
    bc = binary_r(C, bb)
    ans += ac * (n - bc)
print(ans)