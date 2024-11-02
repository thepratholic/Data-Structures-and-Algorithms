def subs(s, curr, i):
    if i == len(s):
        print(curr)
        return
    subs(s, curr, i+1)
    subs(s, curr + s[i], i+1)

subs("AB", "", 0)