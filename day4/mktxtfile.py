import os

def get_fname():
   while True:
     fname = input('请输入文件名：')
     if not os.path.exists(fname):
         break
     print('该文件名已存在，请重新输入')
   return fname

def get_content():
    content= []
    print('请输入正文，并用end结束')
    while True:
        line = input('>')
        if line == 'end':
            break
        content.append(line)
    return content

def write_file():
   with open(fname,'w') as fobj:
       fobj.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content= get_content()
    write_file(fname, content)