# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
def substitution(string):
    string = re.sub(r'((?<=\s)&&(?=\s))','and', string) 
    string = re.sub(r'(?<=\s)\|\|(?=\s)','or', string)
    return string

N = int(input())
for i in range(N):
    print(substitution(input()))    
