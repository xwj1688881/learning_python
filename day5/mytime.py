import time

t1 = time.localtime()
print(time.localtime())  #返回九元组
print(time.gmtime()) #0时区的九元组
print(time.time()) # 返回时间戳，常用
print(time.mktime(t1)) # 把九元组转换成时间戳
print(time.sleep(1))
print(time.asctime()) # 默认返回当前的UTC时间
print(time.ctime()) # 默认返回当前的UTC时间，常用
print(time.ctime(0)) # 时间戳作为参数
print(time.asctime(t1))
print(time.struct_time('%Y-%m-%d %H:%M:%S')) #常用
print(time.strptime('2018-08-20','%Y-%m-%d')) #转九元组

from datetime import datetime, timedelta
t1 = datetime.now()
t1.year
t1.month
t2 = datetime.today()  # 类似于datetime.now，只是参数不一样
datetime.strptime('2018-8-20', '%Y-%m-%d')  # 返回datetime对象

dt = timedelta(days=100)
t1 - dt
t1 + dt