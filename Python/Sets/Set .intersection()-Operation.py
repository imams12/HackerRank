# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_n = set(input().split())
b = int(input())
set_b = set(input().split())
hasil = set_n.intersection(set_b)
print(len(hasil))
