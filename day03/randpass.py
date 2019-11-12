import random
import string
def randpass(num=8):
    all_chs = string.ascii_letters + string.digits
    result = ''
    for i in range(num+1):
        ch = random.choice(all_chs)
        result += ch
    return result

print(randpass(7))