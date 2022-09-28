from itertools import combinations

N = int(input())
s = input().replace(' ','')
K = int(input())
A = list(combinations(s, K))
H = [i for i in A if 'a' in i]
print(len(H)/len(A)) 
