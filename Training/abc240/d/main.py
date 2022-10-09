n = int(input())
alist = list(map(int, input().split()))
stack=[[-1, 0]]
ans = 0
for i in range(n):
    ans += 1
    if stack[-1][0] == alist[i]:
        stack[-1][1] += 1
    else:
        stack.append([alist[i], 1])
    if stack[-1][0] == stack[-1][1]:
        stack.pop()
        ans -= alist[i]
    print(ans)
        

