# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
def findAll(string):
    pattern = r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
    matches = re.finditer(pattern, string)
    
    b = False
    for match in matches:
        group = match.group() 
        n= len(group) 
        print(group[1:n])
        b = True
    if not b:
        print(-1)

findAll(input())        
