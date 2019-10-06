# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
for _ in range(int(input())):
    n, queue = int(input()), deque(list(map(int, input().split())))
    prev = 2**32
    b = True
    while queue:
        if prev >= queue[0] or prev >= queue[-1]: 
            if queue[0] >= queue[-1] and prev>=queue[0]:
                prev = queue.popleft()
            elif queue[-1] >= queue[0] and prev>=queue[-1]:
                prev = queue.pop()
            else:
                b = False
                break
        else:
            b = False
            break
    if not b:
        print("No")
    else:    
        print("Yes")   
