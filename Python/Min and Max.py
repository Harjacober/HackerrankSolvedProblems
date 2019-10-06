import numpy
r,c = tuple(map(int, input().split()))
arr = numpy.array([input().split()  for _ in range(r)], int)
print(numpy.max(numpy.min(arr, axis=1)))
