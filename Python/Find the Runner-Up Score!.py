 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    flag = max(arr)
    maxx = -100 
    for i in arr: 
        if i != flag:
            maxx = max(maxx, i)
    print(maxx)        

