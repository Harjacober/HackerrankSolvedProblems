from collections import deque
d = deque()
for i in range(int(input())):
    arr = input().split()
    eval("d.{}({})".format(*arr,''))
print(*d)
