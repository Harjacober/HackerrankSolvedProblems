import numpy
numpy.set_printoptions(legacy='1.13')
A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A,B))
print(numpy.outer(A,B))
