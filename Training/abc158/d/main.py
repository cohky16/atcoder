from collections import deque
s = input()
q = int(input())

ans = deque(s)
f = False
for i in range(q):
    s = input()
    if s[0] == "2":
        _, ff, c = s.split()
        if ff == "1": 
            if f:
                ans.append(c)
            else:
                ans.appendleft(c)
        else:
            if f:
                ans.appendleft(c)
            else:
                ans.append(c)
    else:
        f = not f
if f:
    ans.reverse()
    print("".join(ans))
else:
    print("".join(ans))
