# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

print(round(math.degrees(math.atan(AB/BC))),chr(176),sep='')
