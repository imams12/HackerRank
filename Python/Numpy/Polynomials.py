import numpy

pol = list(map(float, input().split()))

print(numpy.polyval(pol, int(input())))
