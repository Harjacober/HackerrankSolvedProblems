import re
def decode(string):
    pattern = re.compile(r'(?<=\w)\W+(?=\w)') 
    print(re.sub(pattern, ' ', string))

arr = []
n = list(map(int,input().split()))
row = int(n[0]) 
col = int(n[1]) 
for _ in range(row): 
    arr.append(input())

pro = []    
for i in range(col):
    for j in range(row):
        pro.append(arr[j][i]) 
decode(''.join(pro))
