N, X = list(map(int, input().split()))
arr = []
for i in range(X):
    arr.append(list(map(float, input().split())))
avg = lambda x: sum(x)/len(x)   
print(*map(avg, zip(*arr)), sep='\n')
