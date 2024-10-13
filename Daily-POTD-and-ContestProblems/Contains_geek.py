def contains_geek(s):
    target = "geek"
    j = 0

    for i in range(len(s)):

        if s[i] == target[j]:
            j += 1
        if j == len(target):
            return True

    return False


s = "thegeeks"
print(contains_geek(s))
