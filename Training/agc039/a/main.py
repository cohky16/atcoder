S = input()
K = int(input())

#ランレングス圧縮
def rle(s):
    res = []
    pre = ''
    chain = 1
    for c in s:
        if c == pre:
            chain += 1
        else:
            if pre != '':
                res.append([pre,chain])
            pre = c
            chain = 1
    res.append([pre,chain])
    return res

ans = 0
lis = rle(S)

#1種類の文字列の場合
if len(lis) == 1:
    ans = (lis[0][1] * K) // 2

#2種類以上の文字列の場合
else:
    #先頭と末尾が同じ文字
    if lis[0][0] == lis[-1][0]:
        #先頭、末尾、つなぎ目の対応
        ans += lis[0][1]//2
        ans += lis[-1][1]//2
        lis[0][1] += lis[-1][1]
        lis[-1][1] = 0
        ans += lis[0][1]//2 * (K-1)

        #Sの中での連続文字の対応
        mid_chains = 0
        for i in range(1,len(lis)):
            mid_chains += lis[i][1]//2
        ans += mid_chains * K

    #先頭と末尾が異なる文字
    else:
        mid_chains = 0
        for i in range(len(lis)):
            mid_chains += lis[i][1]//2
        ans += mid_chains * K

print(ans)