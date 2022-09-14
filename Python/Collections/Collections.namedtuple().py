# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
student = namedtuple('Student', input().split())
studentlist=[student(*input().split()) for i in range(n)]
print("%.2f" %(sum([int(studentlist[i].MARKS) for i in range(n)])/n))
