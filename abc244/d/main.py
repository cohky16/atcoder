s = input()
t = input()
yes = "Yes"
no = "No"
if (s == "R G B" and t == "R G B"):
    print(yes)
if (s == "R G B" and t == "R B G"):
    print(no)
if (s == "R G B" and t == "G R B"):
    print(no)
if (s == "R G B" and t == "G B R"):
    print(yes)
if (s == "R G B" and t == "B R G"):
    print(yes)
if (s == "R G B" and t == "B G R"):
    print(no)
if (s == "R B G" and t == "R G B"):
    print(no)
if (s == "R B G" and t == "R B G"):
    print(yes)
if (s == "R B G" and t == "G R B"):
    print(yes)
if (s == "R B G" and t == "G B R"):
    print(no)
if (s == "R B G" and t == "B R G"):
    print(no)
if (s == "R B G" and t == "B G R"):
    print(yes)
if (s == "G R B" and t == "R G B"):
    print(no)
if (s == "G R B" and t == "R B G"):
    print(yes)
if (s == "G R B" and t == "G R B"):
    print(yes)
if (s == "G R B" and t == "G B R"):
    print(no)
if (s == "G R B" and t == "B R G"):
    print(no)
if (s == "G R B" and t == "B G R"):
    print(yes)
if (s == "G B R" and t == "R G B"):
    print(yes)
if (s == "G B R" and t == "R B G"):
    print(no)
if (s == "G B R" and t == "G R B"):
    print(no)
if (s == "G B R" and t == "G B R"):
    print(yes)
if (s == "G B R" and t == "B R G"):
    print(yes)
if (s == "G B R" and t == "B G R"):
    print(no)
if (s == "B R G" and t == "R G B"):
    print(yes)
if (s == "B R G" and t == "R B G"):
    print(no)
if (s == "B R G" and t == "G R B"):
    print(no)
if (s == "B R G" and t == "G B R"):
    print(yes)
if (s == "B R G" and t == "B R G"):
    print(yes)
if (s == "B R G" and t == "B G R"):
    print(no)
if (s == "B G R" and t == "R G B"):
    print(no)
if (s == "B G R" and t == "R B G"):
    print(yes)
if (s == "B G R" and t == "G R B"):
    print(yes)
if (s == "B G R" and t == "G B R"):
    print(no)
if (s == "B G R" and t == "B R G"):
    print(no)
if (s == "B G R" and t == "B G R"):
    print(yes)

