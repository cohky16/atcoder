s = input()
l = len(s) - len(s.lstrip("a"))
r = len(s) - len(s.rstrip("a"))
if l > r: print("No")
else:
    t = "a" * (r - l) + s
    if t == t[::-1]: print("Yes")
    else: print("No")
