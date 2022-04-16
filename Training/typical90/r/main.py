import math
t = int(input())
l,x,y = map(int, input().split())
q = int(input())
for i in range(q):
    e = int(input())
    # 度からラジアンに変換
    rad = math.radians((360/t)*e-90)
    # 観覧車の位置
    Y = - l/2 * math.cos(rad)
    Z = l/2 + l/2 * math.sin(rad)
    d = math.sqrt(((x - 0) ** 2 + (Y - y) ** 2))
    # 俯角
    dep = math.atan2(Z, d)
    # 度に戻す
    print(math.degrees(dep))
