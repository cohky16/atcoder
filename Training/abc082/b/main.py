s = ''.join(sorted(input()))
t = ''.join(sorted(input(), reverse=True))
r = "No"
c = 0
for i in range(min(len(s), len(t))):
    if s[i] > t[i]:
        break
    elif s[i] < t[i]: 
        r = "Yes"
        break
    else: c += 1
if c == len(s) and len(s) < len(t):
    print("Yes")
else:
    print(r)