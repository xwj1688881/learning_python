fobj = open('E:/git_cored/mima.txt') #不指定打开模式，以r模式打开
data = fobj.read()  #read默认读取全部内容
print('data:', data) #打印内容
data2 = fobj.read() #因为文件指针已经移动到尾部，没有数据可读，所以data是空串
print('data2', data2)
fobj.close()

fobj = open('E:/git_cored/mima.txt')
data3 = fobj.read(4) #指定读取4字节，建议一次读1024的倍数
print('data3:', data3)
fobj.close()
fobj = open('E:/git_cored/mima.txt')
data4 = fobj.readline() #适合文本文件，读一行
print('data4:', data4)
data5 = fobj.readlines() #适合文本文件，把所有行读到列表中
print('data5:', data5)
fobj.close()

fobj = open('E:/git_cored/mima.txt')
for line in fobj:
    print('line:', line, end='')
fobj.close()

fobj = open('E:/git_cored/mima.txt', 'w') #w表示 文件存在则清空，不存在则创建
fobj.write('Hello World\n')  #写数据是，先放到缓冲区
                             # 当数据量达到一定程度是，自动写入磁盘

fobj.flush()   #立即将数据同步至磁盘
fobj.writelines(['10 line\n', 'new line\n'])
fobj.close()  #关闭文件时，数据自动写入磁盘

with open('E:/git_cored/mima.txt') as fobj: #with语句结束，文件自动关闭
    print(fobj.readline())


fobj = open('E:/git_cored/mima.txt','rb') #文本文件要加上b,文本文件也可以加b，表示bytes
pointer = fobj.tell() #返回文本指针的位置
print('pointer:', pointer)
pointer = fobj.seek(10, 0) #第一个数字是偏移量，第二个数字是相对位置，0表示开头，1是当前，2是结尾
print('pointer:', pointer)
pointer = fobj.read(4) #从当前位置读4字节，因为是bytes方式打开，所以显示b' xxx'
print('pointer:', pointer)
pointer = fobj.seek(-5, 2) #移动到文件倒数第五个字节的位置。以‘rb’ 才能写负数，‘r’ 不行
print('pointer:', pointer)


import sys

a = sys.stdin.readline()  # 读取键盘输入，回车也作为一个字符\n读入
print(a)
sys.stdout.write(a)
sys.stderr.write(a)