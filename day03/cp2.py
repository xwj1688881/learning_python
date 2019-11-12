def cp2_func(socfile_path,desfile_path):
    with open(socfile_path,'rb') as socfile:
        with open(desfile_path,'wb') as desfile:
            while True:
                copydata = socfile.read(8)
                if not copydata:
                    break
                desfile.write(copydata)

cp2_func('E:/git_cored/mima.txt', 'E:/git_cored/mima2.txt')