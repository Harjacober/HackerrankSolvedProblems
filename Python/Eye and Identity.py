import numpy
a,b = tuple(map(int, input().split()))
print(str(numpy.eye(a,b, k=0)).replace("1"," 1").replace("0"," 0"))
