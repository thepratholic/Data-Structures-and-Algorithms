from collections import deque
d = deque()

d.append(10)
d.append(20)

d.appendleft(2)

print(d.pop())
print(d.popleft())

d.insert(1, 30)

print(d.index(30))

print(d.count(30))

d.appendleft(1)

d.remove(1)

d.extend([4,5,6])

d.extendleft([7,8,9])

d.rotate(2) #rotates two times by right

d.reverse()

print(d)