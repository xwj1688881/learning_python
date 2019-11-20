import sys
def text_u2d(fname):
   des_fname = fname + '.txt'
   scr_file = open(fname)
   des_file = open(des_fname)
   for line in scr_file:
       line = line.rstrip() + '\r\n' #rstrip:将字符右边的空白去除  \r：将光标回退至本行开头位置 \n:下一行
       des_file.write(line)



if __name__ == '__main__':
    text_u2d(sys.argv[1])