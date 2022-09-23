# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(input().split())
b = int(input())
B = set(input().split())
hasil = A.union(B)
count = 0
for i in hasil:
  count +=1
print(count)
