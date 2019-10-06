from collections import OrderedDict
from heapq import nlargest


if __name__ == '__main__':
    s = input()
    dic = OrderedDict()
    for e in s:
        dic[e] = dic.get(e, 0) + 1
    arr = sorted(dic.items(), key=lambda x:(-x[1],x[0]))
    for i in arr[0:3]: 
        print(*i)  
