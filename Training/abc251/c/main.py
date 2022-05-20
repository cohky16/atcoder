n = int(input())
s,t = input().split()
dict = dict({s: {"index": 1, "point": t}})
for i in range(n-1):
    s,t = input().split()
    if s in dict: continue
    dict[s] = {"index": i + 2,  "point": t}
ans = 0
max = 0
for v in dict.values():
    if max < int(v["point"]):
        ans = int(v["index"])
        max = int(v["point"])
print(ans)