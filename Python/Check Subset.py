T = int(input())
for _ in range(T):
    arr = [set(input().split()) if j%2!=0 else input() for j in range(4)] 
    print(arr[1].issubset(arr[3]))
