import pickle as p
# pickle存储器可以将任意的数据类型写入文件，还可以无损的取出

shop_file = 'E:/git_cored/shop_list.txt'
shop_list = ['apple', 'banana', 'egg']
with open(shop_file, 'wb') as fobj:
    p.dump(shop_list, fobj) #将列表写入文件
    
with open(shop_file, 'rb') as fobj:
    mylist  = p.load(fobj) #从文件中取出的数据仍然是列表

print(mylist[1])