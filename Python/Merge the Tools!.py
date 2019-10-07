def merge_the_tools(string, k):
    dic = {}
    arr = []
    for i in range(len(string)):
        if string[i] not in dic:
            dic[string[i]] = True
            arr.append(string[i])
        if (i+1)%k == 0:    
            print(''.join(arr))
            dic.clear()
            arr.clear()
