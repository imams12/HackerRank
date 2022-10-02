n = int(input())
list_n = list(map(int, input().split()))
print(all([i >= 0 for i in list_n]) and any([str(i)==str(i)[::-1] for i in list_n]))
