try:
    num = int(input('number:'))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('输入错误')
except (KeyboardInterrupt, EOFError):
    print('\nBYEBYE')
else:
    print(result) #不发生异常才执行的代码
finally:
    print('DONE') #不管异常是否发生都要执行的代码


#NameError           未申明/初始化对象
#IndexError          序列中没有此索引
#SyntaxError         语法错误
#KeyboardInterrupt   用户中断执行
#EOPError            没有内建输入，到达EOF标记
#IOError             输入/输出操作失败