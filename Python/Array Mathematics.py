import numpy
row, col = tuple(map(int, input().split()))
a = numpy.array([input().split() for _ in range(row)], int)
b = numpy.array([input().split() for _ in range(row)], int)
print(*[a+b,a-b,a*b,a//b,a%b,a**b], sep="\n")
