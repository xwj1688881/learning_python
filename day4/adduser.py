import sys
import subprocess
from randpass import randpass


def adduser(username,password,fname):
   user_info = '''user information:
   username: %s
   passworf: %s
   '''% (username , password)
   subprocess.call('useradd %s' % username, shell=True)
   subprocess.call(
       'echo %s | password --stdin %s' % (password , username),
       shell=True
    )
   with (fname, 'a') as fobj:
       fobj.write(user_info)




if __name__ == '__main__':
    password = randpass()
    username = sys.argv[1]
    adduser(username, password, '/tmp/user.txt')