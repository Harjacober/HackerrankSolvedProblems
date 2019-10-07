if __name__ == '__main__':
    a = []
    N = int(input())
    for _ in range(N):
        func, *arg = input().split() 
        if func != "print":    
            eval("a.{}({})".format(func,','.join(arg)))
        else:
            print(a)
