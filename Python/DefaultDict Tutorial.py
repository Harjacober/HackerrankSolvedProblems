from collections import defaultdict
n, m = list(map(int, input().split()))
dic = defaultdict(list)
for i in range(n):
    dic[input()].append(i+1)
ans = (dic[input()] for j in range(m))
for each in ans:
    if len(each) == 0:
        print(-1)
    else:
        print(*each)
