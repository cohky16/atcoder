s = input()
c = 0
l = len(s)
a = s.index("A")
z = ''.join(reversed(s)).index("Z")
print(l - z - a)