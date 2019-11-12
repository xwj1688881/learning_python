

def cp_func_1(socfile_path, desfile_path):
    # socfile_path = "'{}'".format(socfile_path)
    # desfile_path = "'{}'".format(desfile_path)
    file1 = open(socfile_path, 'rb')
    file2 = open(desfile_path, 'wb')
    copy_data = file1.read()
    file2.write(copy_data)
    file1.close()
    file2.close()


cp_func_1('E:/git_cored/mima.txt', 'E:/git_cored/mima1.txt')