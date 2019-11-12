


def  multi_table(column):
  for i  in  range(1, column+1) :
      for j in range(1,i+1):
          print('%s*%s=%s' %(i, j, i*j), end=' ')
      print()



multi_table(11)