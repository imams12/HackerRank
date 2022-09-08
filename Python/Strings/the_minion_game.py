def minion_game(string):
    Kevin_point = 0
    Stuart_point = 0
    for i in range(len(string)):
      if string[i] not in ('A','I','U','E','O'):
        Stuart_point = Stuart_point + len(string) - i
      else:
        Kevin_point = Kevin_point + len(string) - i
    if (Stuart_point > Kevin_point):
      print('Stuart', Stuart_point)
    elif (Kevin_point > Stuart_point):
      print('Kevin', Kevin_point)
    else:
      print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
