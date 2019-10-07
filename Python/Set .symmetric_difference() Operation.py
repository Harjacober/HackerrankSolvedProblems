arr = [set(input().split()) if i%2!=0 else input() for i in range(4)] 
print(len(arr[1] ^ arr[3]))
