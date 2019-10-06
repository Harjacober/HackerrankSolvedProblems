n = int(input())
e = input().split()
dic = {}
for i in e:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(*filter(lambda x:dic[x]==1, dic)) 
