print(list('abcd'))
print(list((10,20,30)))
print(tuple('abcd'))
print(str(100))
print(str((10, 20, 30)))
print([str(100) for i in range(4)])
print(max([10, 20, 30]))
print(min([10, 20, 30]))
print(max('hello'))


users = ['bob', 'alice', 'john']
print('range(len)方式')
for i in range(len(users)):
    print('%s: %s' % (i, users[i]))

print('enumerate方式：')
print('list(enumerate(users):' , list(enumerate(users)))
for item in enumerate(users):
    print('%s: %s' % (item[0],item[1]))

for i, j in enumerate(users):
    print('%s : %s' % (i, j))


for u in reversed(users):
    print(u)


for u in sorted(users):
    print(u)