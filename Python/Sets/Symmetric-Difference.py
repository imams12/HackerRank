# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))
hasil1 = a.difference(b)
hasil2 = b.difference(a)
hasil1.update(hasil2)
new_hasil = sorted(hasil1)
for i in new_hasil:
  print(i)
