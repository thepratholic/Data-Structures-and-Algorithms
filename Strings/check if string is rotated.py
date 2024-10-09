# Check if string is rotated

def arerotations(s1,s2) :
    if len(s1) != len(s2) :
        return False
    temp = s1 + s1
    if s2 in temp: return True
    else: return False

s1 = "ABDC"
s2 = "DABC"

print(arerotations(s1,s2))