import sys
def nonRep(s):
    count = [-1] * 256
    res = sys.maxsize

    for i in range(len(s)):
        if count[ord(s[i])] == -1:
            count[ord(s[i])] = i
        else:
            count[ord(s[i])] = -2

    for i in range(256):
        if count[i] >= 0:
            res = min(res, count[i])

    if res == sys.maxsize: return -1
    return res

print(nonRep("apple"))