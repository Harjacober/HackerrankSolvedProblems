import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(input().rstrip().split())) 

    k = int(input())
    arr.sort(key=lambda x:int(x[k]))
    for each in arr:
        print(*each)
