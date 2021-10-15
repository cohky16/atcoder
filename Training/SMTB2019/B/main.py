n = int(input())
i = int(-(-n // 1.08))
print(i if int(i * 1.08) == n else ":(")