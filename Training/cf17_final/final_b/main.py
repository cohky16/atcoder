from collections import Counter
s = list(input())
c = list(Counter(s).values())
if len(c) != 3: c.append(0)
print("YES" if max(c) - min(c) <= 1 else "NO")