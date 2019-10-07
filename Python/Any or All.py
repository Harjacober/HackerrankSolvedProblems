n = int(input())
s = input().split()
print(all(map(lambda x:int(x)>0, s)) and any(map(lambda x:x==x[::-1], s)))
