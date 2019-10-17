# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def start(S,K):  
    pattern = re.compile(r'(?={k})'.format(k=K))
    matches = re.finditer(pattern, S)
    b = False
    for match in matches:
        b = True
        print((match.start(), match.end()+len(K)-1))    
    if not b:
        print((-1,-1))

S = input()
K = input()
start(S,K)
