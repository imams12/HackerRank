import numpy

def arrays(arr):
    a = numpy.array(arr[::-1], float)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
