# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def validHex(string):
    brace_pattern = r'{[\w\W]*?}'
    selectors = re.finditer(brace_pattern, string)
    pattern = r'#([1234567890ABCDEFabcdef]{3}|[1234567890ABCDEFabcdef]{6})\b'
    for selector in selectors:
        matches = re.finditer(pattern, selector.group()) 
        for match in matches:
            print(match.group())
        
n = int(input())
arr = []
for i in range(n):
    arr.append(input())

validHex('\n'.join(arr))  

