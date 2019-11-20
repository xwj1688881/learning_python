from string import ascii_letters , digits
from keyword import iskeyword

idt = 'abc_123'
for i, j in enumerate(idt[0:]):
    print('%s  :%s' % (i, j))


def check_id(idt):
    first_chs = ascii_letters + '_'
    other_chs = first_chs + digits
    if iskeyword(idt):
        return '%s is keyword' % (idt)
    if idt[0] not in   first_chs:
        return '%s is 1st invalid'
    for i, j in enumerate(idt[1:]):
        if j not in other_chs:
            return '第%s个字符不合法' % (i + 2)

    return '%s是合法的' % idt

