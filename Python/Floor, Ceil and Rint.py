import numpy
numpy.set_printoptions(sign=' ')
arr = numpy.array(input().split(), float)
print(numpy.floor(arr), numpy.ceil(arr), numpy.rint(arr), sep="\n")
