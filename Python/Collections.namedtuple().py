from collections import namedtuple# Enter your code here. Read input from STDIN. Print output to STDOUT
n,Student = int(input()), namedtuple('Students',input()) 
std = [int(Student(*input().split()).MARKS) for i in range(n)]
print("{0:.2f}".format(sum(std)/len(std)))
 
