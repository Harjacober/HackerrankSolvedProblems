from itertools import combinations
def probability(string, k):
    num = 0
    den = 0
    for each in combinations(string, int(k)):
        if "a" in each:
            num += 1
        den += 1
    ans = num/den        
    print("{0:.5f}".format(ans))
n = int(input())
s = input().split()
k = int(input())
probability(s,k)
