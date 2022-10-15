from collections import Counter


n = int(input())
clist = input()
rcount = sum([1 for c in clist if c == 'R'])
print(sum([1 for c in clist[:rcount] if c == 'W']))