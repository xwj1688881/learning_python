stack = []

def push_it():
    item = input('item to push:')
    stack.append(item)

def pop_it():
    if stack:
        print('pop: %s' % stack.pop())


def view_it():
    print('%s' % stack)

def show_menu():
    cmds ={'0':push_it , '1':pop_it, '2':view_it}
    menu = '''(0)push_it
    (1)pop_it
    (2)view_it
    please input your choice(0/1/2/3):'''
    while True:
        choice = input(menu).strip()[0]
        if choice not in '0123':
            print('Invalid input. Try again.')
            continue
        if choice == '3':
            break
        cmds[choice]()
if __name__ == '__main__':
    show_menu()