import numpy
numpy.set_printoptions(legacy='1.13')
r = int(input())
a = numpy.array([input().split()  for _ in range(r)], int)
b = numpy.array([input().split()  for _ in range(r)], int)
print(numpy.dot(a,b))
