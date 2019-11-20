from getpass import getpass

userdb = {}

def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if userdb.get(username) != password:
        print("用户名或密码错误")
    elif userdb.get(username) == password:
        print("登录成功")




def register():
    username = input("请输入注册用户名：")
    if username not in userdb:
     password = input("请输入注册密码：")
     userdb[username] = password
    else:
     print("已有重复用户名，请再次输入")




def show_menu():
    cmds = {'0':register, '1':login}
    menu = '''[0]:注册用户
    [1]:登录用户
    [2]:退出
    请输入0/1/2：
    '''
    while True:
      choice = input(menu).strip()[0]
      if choice not in '012':
          continue

      if choice == '2':
          break

      cmds[choice]()

if __name__ == '__main__':
    show_menu()
