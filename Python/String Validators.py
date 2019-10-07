if __name__ == '__main__':
    s = input()
    arr = [str.isalnum,str.isalpha,str.isdigit,str.islower,str.isupper]  
    for i in arr:
        print(any([i(c) for c in s]))
