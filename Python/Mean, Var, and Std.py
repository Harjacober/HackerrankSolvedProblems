import numpy
numpy.set_printoptions(legacy='1.13')
r,c = tuple(map(int, input().split()))
arr = numpy.array([input().split()  for _ in range(r)], int)
print(numpy.mean(arr, axis=1), numpy.var(arr, axis=0),numpy.std(arr,axis=None),sep="\n")
