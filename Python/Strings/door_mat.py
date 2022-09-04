pattern = '.|.'
a, b = map(int, input().split())

for i in range(1,a,2):
  print((pattern*i).center(b, '-'))
  
print('WELCOME'.center(b,'-'))
  
for i in reversed(range(1,a,2)):
  print((pattern*i).center(b, '-'))
