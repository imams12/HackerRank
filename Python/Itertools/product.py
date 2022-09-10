## Solution 1
from itertools import product

A = map(int, input().split())
B = map(int, input().split())

hasil = list(product(A,B))

for i in range(len(hasil)):
    print(hasil[i], end = ' ')
    
## Solution 2
from itertools import product

A = map(int, input().split())
B = map(int, input().split())

hasil = list(product(A,B))
print(*hasil)   # * -> menghilangkan koma dan kurung siku pada list dan tuple
