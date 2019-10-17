# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
def parse(string):
    emailAdress = email.utils.parseaddr(string)[1] 
    pattern = re.compile(r'([A-Za-z][A-Za-z_.0-9-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})$')
    match = re.match(pattern, emailAdress) 
    if bool(match):
        print(string)

n = int(input())
for i in range(n):
    parse(input())
