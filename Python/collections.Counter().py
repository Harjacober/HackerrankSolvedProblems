from collections import Counter
n, shoesizedic = int(input()), Counter(list(map(int,input().split())))
total = 0
for i in range(int(input())):
    size, price = list(map(int, input().split()))
    #bool of zero is False 
    if shoesizedic[size]:
        total += price
        shoesizedic[size] -= 1
print(total)
