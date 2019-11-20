adict = dict(['ab', 'cd', ('abc','efg')])
print(adict)
bdict = {}.fromkeys(['ben', 'alice', 'gay'], 7)
print(bdict)

for key in bdict:
    print('%s : %s ' % (key , bdict[key]))

print('%(ben)s' % bdict)

bdict['ben'] = 8 #ben已经是字典的key,更新值
bdict['abc'] = 10 #john没在字典中，新增一项
print(bdict)
bdict.pop('ben')
7 in bdict #返回false
'alice' in bdict #返回true

cdict = bdict.copy() #将bdict的内容赋值给cdict,cdict使用全新的内存空间
bdict.get('bob') #返回bob对应的value,如果没有bob,默认返回None
bdict.get('jane','not found') #如果没有jane,返回not found
print(bdict)
bdict.setdefault('bob',10) #bob已经是字典的key,返回value
bdict.setdefault('jane',10) #jane没在字典中，向字典中写入
print(list(bdict.keys()))
print(list(bdict.values()))
print(list(bdict.items()))
bdict.update({'aaa':'111' ,'bbb':'222'}) #合并字典
print(bdict)
