n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
  command, *k = input().split()
  if command == 'remove':
    s.remove(int(*k))
  elif command == 'discard':
    s.discard(int(*k))
  elif command == 'pop':
    s.pop()
print(sum(s))
