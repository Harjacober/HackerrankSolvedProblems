from itertools import combinations_with_replacement
string, k = input().split()
string = sorted(string)
print(*[''.join(each) for each in combinations_with_replacement(string, int(k))], sep="\n")

