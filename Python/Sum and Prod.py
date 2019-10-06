import numpy
row, col = tuple(map(int, input().split()))
arr =  numpy.array([input().split() for _ in range(row)], int)
print(numpy.prod(numpy.sum(arr, axis=0)))
