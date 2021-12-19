def find(par, x):
    if par[x] == x: # 根の判定
        return x
    else:
        par[x] = find(par, par[x]) # 経路圧縮
    return par[x]

def same(par, x, y):
    return find(par, x) == find(par, y)

def unite(par, x, y):
    x = find(par, x)
    y = find(par, y)
    if x == y: return 0
    par[x] = y

n,q = map(int, input().split())
par = [i for i in range(n)] # 根のリスト
for i in range(q):
    com,x,y = map(int, input().split())
    if com == 0: unite(par,x,y)
    else:
        if same(par,x,y):
            print(1)
        else:
            print(0)