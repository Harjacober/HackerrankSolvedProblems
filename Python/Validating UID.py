# Enter your code here. Read input from STDIN. Print output to STDOUT

def validate(string):
    if len(string) != 10:
        return "Invalid"
    ucase = False
    digit = False
    anumeric = True
    repeat = True 
    uCount = 0
    dCount = 0
    for i in range(len(string)):
        if string[i].isupper():
            uCount += 1
        if  string[i].isdigit():
            dCount += 1   
        if not string[i].isalnum():
            anumeric = False
        if string.count(string[i]) > 1:
            repeat = False    
    if uCount >= 2:
        ucase = True
    if dCount >= 3:
        digit = True    
    if digit and ucase and anumeric and repeat:
        return "Valid"
    else:
        return "Invalid"        

n = int(input())
for i in range(n):
    string = input()
    print(validate(string))
