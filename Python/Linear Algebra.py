import numpy
numpy.set_printoptions(legacy="1.13")
arr = numpy.array([input().split() for _ in range(int(input()))], float)
print("{}".format(round(numpy.linalg.det(arr),2))) 

