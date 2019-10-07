n = int(input())
s = set(map(int, input().split()))
k = int(input())
for _ in range(k):
    a = input().split()
    if len(a) == 1:
        s.pop() 
    else:
        getattr(s,a[0])(int(a[1]))  
print(sum(s))
