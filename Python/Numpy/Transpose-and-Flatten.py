import numpy

N, M = map(int, input().split())
data = numpy.array([input().split() for i in range(N)], int)
print(numpy.transpose(data))
print(data.flatten())
