s = input()
ans = "NO"
for i in range(8):
    if s[:i] + s[i-7:] == "keyence":
        ans = "YES"
print(ans)