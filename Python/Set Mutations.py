A = int(input())
a = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    operation = input().split()[0]
    Set = set(map(int, input().split()))
    getattr(a, operation)(Set)  
print(sum(a))
