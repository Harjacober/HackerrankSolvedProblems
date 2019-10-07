from itertools import combinations
string, k = input().split()
string = sorted(string)
for i in range(1,int(k)+1):
    print(*[''.join(each) for each in combinations(string, i)], sep="\n")
