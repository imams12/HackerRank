import numpy
N, M, P = map(int, input().split())
array_1 = numpy.array([input().split() for i in range(N)], int)
array_2 = numpy.array([input().split() for i in range(M)], int)
print(numpy.concatenate((array_1, array_2), axis=0))
