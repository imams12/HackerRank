import numpy

N, M = map(int, input().split())
A=numpy.array([list(map(int, input().split())) for i in range(N)])
B=numpy.array([list(map(int, input().split())) for i in range(N)])
print(A+B, A-B, A*B, A//B, A%B, A**B, sep="\n")
