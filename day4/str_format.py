'%s is %s years old' % ('bob', 25)
'%s is %d years old' % ('bob', 25)
'%12s%8s' % ('name', 'age')
'%12s%8s' % ('bob', 25)
'%-12s%-8s' % ('name', 'age')
'%-12s%-8s' % ('bob', 25)
#############以下内容不常用################
'%c' % 98  # ascii为98的字符
'%#o' % 30  # 8进制数形式
'%#x' % 30  # 16进制数形式
'%e' % 100000  # 科学计数法
'%f' % (5 / 3)  # 浮点数
'%.2f' % (5 / 3)  # 小数占两位
'%5.2f' % (5 / 3)  # 总宽度为5，小数占两位
'%+d' % 10  # 正数前加上+号
'%+d' % -10
'% d' % 10  # 正数前加空格
'% d' % -10
'%010d' % 55  # 总宽度为10，不够宽度前面补0
############################
'{} is {} years old'.format('bob', 25)
'{1} is {0} years old'.format(25, 'bob')
'{:<20}'.format('hello')
'{:>20}'.format('hello')
'{:^20}'.format('hello')
