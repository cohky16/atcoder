n = int(input())
l = []
for i in range(n):
    s, p = input().split()
    l.append({
        "index": i + 1,
        "simei": s,
        "point": int(p)
    })
for i in sorted(l, key=lambda x: (x["simei"], -x["point"])):
    print(i["index"])