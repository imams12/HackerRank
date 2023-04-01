import numpy

N, M = map(int, input().split())
A=numpy.array([list(map(int, input().split())) for i in range(N)])
print(numpy.max(numpy.min(A, axis=1)))
