import numpy
row, column = list(map(int, input().split()))
arr = numpy.array([list(map(int, input().split())) for _ in range(row)]) 
print(numpy.transpose(arr))
print(arr.flatten())
