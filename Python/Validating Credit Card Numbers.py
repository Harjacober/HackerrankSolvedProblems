# Enter your code here. Read input from STDIN. Print output to STDOUT
#note, i just decided to solve it without regex, using regex is the best way to solve this problem
import re
def repeated(string):
    count = 1
    for i in range(len(string)): 
        if count >= 4:
            return False 
        if string[i] == string[i-1]:
            count += 1
        else:
            count = 1
    return True
def solution(string):
    a = string[0]
    if (a != "4" and a != "5" and a != "6"):
        return "Invalid"
    if "-" in string:
        if string.count("-") != 3:
            return "Invalid"
        pattern = r'([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)'
        oo = re.findall(pattern,string)
        if len(oo) > 0:
            for i in oo[0]:
                if len(i) != 4:
                    return "Invalid"
            string = "".join(list(oo[0]))
            
        else:
            return "Invalid"
    rep = repeated(string)   
    if not (len(string)== 16 and string.isdigit() and rep):
        return "Invalid"
    return "Valid"

n = int(input())
for i in range(n):
    s = input()
    print(solution(s))        
