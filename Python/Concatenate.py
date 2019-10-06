import numpy
N, M, P = list(map(int, input().split()))
arr1 = numpy.array([input().split() for _ in range(N)], int)
arr2 = numpy.array([input().split() for _ in range(M)], int)
print(numpy.concatenate((arr1, arr2)))
