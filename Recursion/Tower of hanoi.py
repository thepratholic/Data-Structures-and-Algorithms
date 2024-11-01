def TOH(n, a, b, c):
    if n == 1:
        print("Move 1 from", a, " to ", c)
    else:
        TOH(n-1, a, c, b)
        print("Move", n, " from ", a, " to ", c)
        TOH(n-1, b, a, c)
TOH(2, "A", "B", "C")