from random import choice
from string import ascii_letters , digits

def randpass(num=8):
  all_chs = ascii_letters + digits
  result = [choice(all_chs) for i in range(num)]
  return ''.join(result)


print(randpass(10))