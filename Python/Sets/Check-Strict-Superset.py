# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
  set_n = set(map(int, input().split()))
  if A.intersection(set_n) == set_n:
    Hasil = True
  else:
    Hasil = False
    break

print(Hasil)
