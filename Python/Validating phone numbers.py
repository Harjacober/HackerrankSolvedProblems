# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def validate(string): 
    pattern = re.compile(r'[789][0-9]{9}$')
    if bool(re.match(pattern, string)):
        print("YES")
    else:
        print("NO")

n = int(input())
for i in range(n):
    validate(input())        
