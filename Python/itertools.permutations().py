from itertools import permutations
string, k = input().split() 
lis = permutations(sorted(string), int(k))
for each in lis:
    print(''.join(each))
    
