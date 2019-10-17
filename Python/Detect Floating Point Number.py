# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def detect(string):
    pattern = re.compile(r'^[-+]?[0-9]*\.[0-9]+$')
    match = re.match(pattern, string) 
    return bool(match)

T = int(input())
for i in range(T):
    string = input()
    print(detect(string))  
