from random import choice
from string import ascii_letters , digits


#随机字母数字组成几位密码
def randpass(num = 8):
    result = ''
    all_chs = ascii_letters + digits
    for i in range(num):
        ch = choice(all_chs)
        result += ch
    return result


# print(randpass(7))
