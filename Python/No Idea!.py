n,m,a,b = input(), input().split(), set(input().split()), set(input().split())
happiness = 0
for e in m:
    if e in a:
        happiness += 1
    if e in b:
        happiness -= 1    
print(happiness)
