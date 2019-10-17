# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def groups(string):
    pattern = r'([A-Za-z0-9])\1'
    match = re.findall(pattern, string) 
    if match:
        return match[0]
    else:
        return -1
print(groups(input()))
