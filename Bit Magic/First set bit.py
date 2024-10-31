def setOrNot(s):
    pos = 1
    while (s & 1) == 0:
        s >>= 1
        pos += 1
    print(pos)

setOrNot(18)