import numpy

N = int(input())
A=numpy.array([list(map(int, input().split())) for i in range(N)])
B=numpy.array([list(map(int, input().split())) for i in range(N)])
print(numpy.dot(A, B))
