import os


os.getcwd() #pwd
os.listdir() #ls
os.listdir('/tmp/mydemo') #ls /tmp/mydemo
os.mkdir('/tmp/mydemo')
os.chdir('/tmp/mydemo')
os.mknod('mytest') # touch mytest
os.symlink('/etc/hosts','zhuji') # In -s /etc/hosts zhuji
os.makedirs('aaa/bbb/ccc') #mkdir -p aaa/bbb/ccc
os.path.isfile('zhuji')
os.path.isdir('/tmp')
os.path.exists('/abc')
os.path.abspath('zhuji') #返回绝对路径
os.path.basename('/tmp/abc/aaa.txt') #返回文件名
os.path.split('/tmp/abc/aaa.txt') #把路径分割成 dirname 和 basename，返回一个元组
os.path.splitext('/tmp/abc/aaa.txt')  #分割路径，返回路径名和文件扩展名的元组
os.path.join('/tmp','abc') #把目录和文件名合成一个路径
os.remove('mytest')
os.rmdir('aaa/bbb/ccc') #删除空目录
os.chmod('aaa',0o777)