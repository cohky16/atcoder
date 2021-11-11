import re
s = input()
a = []
a.append(re.match(r'.*keyence', s))
a.append(re.match(r'k.*eyence', s))
a.append(re.match(r'ke.*yence', s))
a.append(re.match(r'key.*ence', s))
a.append(re.match(r'keye.*nce', s))
a.append(re.match(r'keyen.*ce', s))
a.append(re.match(r'keyenc.*e', s))
a.append(re.match(r'keyence.*', s))
print("YES") if a.count(None) != 8 else print("NO")
