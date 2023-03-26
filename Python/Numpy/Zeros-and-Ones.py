import numpy

dimension = tuple(map(int, input().split()))
print(numpy.zeros(dimension, dtype=numpy.int64))
print(numpy.ones(dimension, dtype=numpy.int64))
