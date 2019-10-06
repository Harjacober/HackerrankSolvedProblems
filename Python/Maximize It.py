from itertools import product# Enter your code here. Read input from STDIN. Print output to STDOUT
K, M = list(map(int, input().split()))
ans = 0
alllist = (list(map(int, input().split()))[1::] for i in range(K)) 
print(max(map(lambda x:sum(i**2 for i in x)%M,product(*alllist))))
