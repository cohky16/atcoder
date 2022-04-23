S = input()
a=False
b=False
for c in S:
    if c.islower(): a = True
    if c.isupper(): b = True
t = set(list(S))
c=True if len(t) == len(S) else False
print("Yes" if a and b and c else "No")