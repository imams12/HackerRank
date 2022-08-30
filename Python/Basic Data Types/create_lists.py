if __name__ == '__main__':
  arr = []  
  N = int(input())
  for i in range(N):
    command, *line = input().split()
    if command == "insert":
      i, e = map(int,line)
      arr.insert(i,e)
    elif command == "remove":
      arr.remove(int(line[0]))
    elif command == "append":
      arr.append(int(line[0]))
    elif command == "sort":
      arr.sort()
    elif command == "pop":
      arr.pop()
    elif command == "reverse":
      arr.reverse()
    elif command == "extend":
      arr.extend(list(map(int, line)))
    elif command == "count":
      arr.count()
    elif command == "index":
      arr.index(int(line[0]))
    else:
      print(arr)
